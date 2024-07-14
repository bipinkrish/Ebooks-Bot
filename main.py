import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton, InputMediaPhoto, Message
from buttons import getButtons, getButtonsIA, getSrc
import pdfdrive
import libgen
import annas
import hunter
import zlibrary
from openlibrary import openlibrary
import scihub
import json
from typing import List, Dict


with open('config.json', 'r') as f: data = json.load(f)
def getenv(var): return os.environ.get(var) or data.get(var, None)

bot_token = getenv("TOKEN")
api_hash = getenv("HASH")
api_id = getenv("ID")

if bot_token is None or api_hash is None or api_id is None:
    print("Required ENVs are not set i.e TOKEN, HASH, ID")
    exit(1)

wrongimage = "https://i.ibb.co/9pBPB5S/wrong.png"
noimage = "https://t3.ftcdn.net/jpg/04/34/72/82/360_F_434728286_OWQQvAFoXZLdGHlObozsolNeuSxhpr84.jpg"
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

# zlibrary
remix_id = getenv("REMIX_ID")
remix_key = getenv("REMIX_KEY")
zemail = getenv("Z_EMAIL")
zpass = getenv("Z_PASS")
zlib_multi: List[Dict] = getenv("ZLIB_MULTI")

Z: zlibrary.Zlibrary = None
ZM: List[zlibrary.Zlibrary] = []
Z_INDEX = -1

def loopZ():
    if not ZM: return
    global Z, Z_INDEX

    for _ in range(len(ZM)):        
        Z_INDEX += 1
        Z = ZM[Z_INDEX % len(ZM)]

        downloads_left = Z.getDownloadsLeft()
        if downloads_left > 0:
            print("Switching Zlibrary account")
            print("Switched to: ", Z._Zlibrary__email)
            print("Downloads left: ", downloads_left)
            break
    else:
        print("All Zlibarary accounts have 0 downloads left.")

if not zlib_multi:
    if remix_id is not None and remix_key is not None: Z = zlibrary.Zlibrary(remix_userid=remix_id, remix_userkey=remix_key)
    elif zemail is not None and zpass is not None: Z = zlibrary.Zlibrary(email=zemail, password=zpass)
    if Z and not Z.isLogin(): raise("Wrong Credentials")
else:
    for account in zlib_multi:
        keys = account.keys()
        if "email" in keys and "password" in keys:
            login = zlibrary.Zlibrary(email=account["email"], password=account["password"])
            if login.isLogin(): ZM.append(login)
        elif "remix_id" in keys and "remix_key" in keys:
            login = zlibrary.Zlibrary(remix_userid=account["remix_id"], remix_userkey=account["remix_key"])
            if login.isLogin(): ZM.append(login)
    
    print("Zlibrary accounts loaded: ", len(ZM))
    loopZ()
    

# open library
iaemail = getenv("IA_EMAIL")
iapass = getenv("IA_PASS")

data = {}
site = {}
Null = "Null"
def storedata(msgid,books,website):
    data[msgid] = books
    site[msgid] = website

def getdata(msgid):
    return data.get(msgid,None), site.get(msgid,None)

def removedata(msgid):
    data[msgid] = Null
    site[msgid] = Null


sites = ["librarygenesis", "zlib", "openlib", "scihub", "annas", "pdfdrive", "hunter"]
def isSite(calldata):
    for ele in sites:
        if ele in calldata: return True
    return False


@app.on_message(filters.command(["start","help"]))
def echo(client: Client, message: Message):
    app.send_message(message.chat.id,
        f"__Hello {message.from_user.mention}, \
I am Ebooks Finder Bot, Just send me a name of the Book and I will get you results from \
[Library Genesis](https://libgen.li/), \
[Zlibrary](http://z-lib.org/), \
[OpenLibrary](https://openlibrary.org)/[InternetArchive](https://archive.org/), \
[SciHub](https://sci-hub.se/), \
[Anna's Archive](https://annas-archive.org/), \
[PdfDrive](https://pdfdrive.to), \
and [eBook-Hunter](https://ebook-hunter.org/), \
to right here OR send me ACSM file from IA to decrypt__", reply_to_message_id=message.id, disable_web_page_preview=True,
reply_markup=getSrc())


def handleASCM(file, message: Message):
    msg: Message = app.send_message(message.chat.id, "__Processing__", reply_to_message_id=message.id)
    try: ofile = openlibrary.acsm(file,None)
    except: ofile is None
    os.remove(file)

    if ofile is not None:
        app.edit_message_text(message.chat.id, msg.id, "__Uploading__")
        app.send_document(message.chat.id, ofile, reply_to_message_id=message.id)
        app.delete_messages(message.chat.id, msg.id)
        os.remove(ofile)
    else:
        app.edit_message_text(message.chat.id, msg.id, "__Failed, problem in Decrypting__")


@app.on_message(filters.document)
def acsmfile(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    if message.document.file_name.split(".")[-1].lower() == "acsm":
        file = app.download_media(message)
        handleASCM(file, message)


@app.on_message(filters.text)
def bookname(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, '__choose website to get result from__', reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton( text='Library Genesis', callback_data=f"librarygenesis {message.chat.id} {message.id}")],
                    [InlineKeyboardButton( text='Zlibrary', callback_data=f"zlib {message.chat.id} {message.id}")],
                    [InlineKeyboardButton( text='Open Library', callback_data=f"openlib {message.chat.id} {message.id}")],
                    [InlineKeyboardButton( text='SciHub', callback_data=f"scihub {message.chat.id} {message.id}")],
                    [InlineKeyboardButton( text='Annas Archive', callback_data=f"annas {message.chat.id} {message.id}")],
                    [InlineKeyboardButton( text='PDF Drive', callback_data=f"pdfdrive {message.chat.id} {message.id}")],
                    [InlineKeyboardButton( text='eBook Hunter', callback_data=f"hunter {message.chat.id} {message.id}")],                    
                ]))
    

@app.on_callback_query()
def handle(client: pyrogram.client.Client, call: pyrogram.types.CallbackQuery):

    # site selection
    if isSite(call.data):
        app.answer_callback_query(call.id,"processing...")
        data = call.data.split()
        message:pyrogram.types.messages_and_media.message.Message = app.get_messages(data[1], int(data[2]))
        search = message.text

        # pdfdrive
        if data[0] == "pdfdrive":
            books = pdfdrive.getpage(search)
            if len(books) == 0:
                app.send_message(message.chat.id,f"__PDFdrive : No results found__", reply_to_message_id=message.id)
            else:
                templst = [books[0]["coverlink"],books[0]["link"],wrongimage]
                for ele in templst:
                    try:
                        msg = app.send_photo(message.chat.id, ele,
                        pdfdrive.getPdfText(books),
                        reply_to_message_id=message.id, reply_markup=getButtons())
                        break
                    except: pass
                storedata(msg.id,books,"pdfdrive")
        
        # librarygenesis
        elif data[0] == "librarygenesis":
            books = libgen.getBooks(search)
            if len(books) == 0:
                app.send_message(message.chat.id,f"__LibraryGenesis : No results found__", reply_to_message_id=message.id)
            else:
                msg = app.send_photo(message.chat.id, libgen.getBookImg(books[0]),
                    libgen.getLibText(books), reply_to_message_id=message.id, reply_markup=getButtons())
                storedata(msg.id,books,"librarygenesis")
        

        # annas archive
        elif data[0] == "annas":
            books = annas.getAnnasBooks(search)
            if books is None:
                app.send_message(message.chat.id,f"__Not able to Connect, maybe Cloudflare protection__", reply_to_message_id=message.id)
            elif len(books) == 0:
                app.send_message(message.chat.id,f"__Annas Archive : No results found__", reply_to_message_id=message.id)
            else:
                msg = app.send_photo(message.chat.id, books[0]["cover"],
                    annas.getAnnasText(books), reply_to_message_id=message.id, reply_markup=getButtons())
                storedata(msg.id,books,"annas")
        
        # ebook hunter
        elif data[0] == "hunter":
            books = hunter.getHunterBooks(search)
            if len(books) == 0:
                app.send_message(message.chat.id,f"__Ebook Hunter : No results found__", reply_to_message_id=message.id)
            else:
                msg = app.send_photo(message.chat.id, books[0]["cover"],
                    hunter.getHuntText(books), reply_to_message_id=message.id, reply_markup=getButtons())
                storedata(msg.id,books,"hunter")

        # zlib
        elif data[0] == "zlib":
            if not Z:
               app.send_message(message.chat.id,f"__Required variables are not set, you can't use Zlibrary__", reply_to_message_id=message.id) 
               return
            
            check, books = zlibrary.getZlibBooks(Z,search)
            if not check:
                app.send_message(message.chat.id,f"__{books}__", reply_to_message_id=message.id)
            elif len(books) == 0:
                app.send_message(message.chat.id,f"__Zlibrary : No results found__", reply_to_message_id=message.id)
            else:
                msg: Message = app.send_photo(message.chat.id, zlibrary.getImage(Z, books[0]),
                    zlibrary.getZlibText(books), reply_to_message_id=message.id, reply_markup=getButtons())
                storedata(msg.id,books,"zlib")    

        # open library
        elif data[0] == "openlib":
            books = openlibrary.getOpenlibbooks(search)
            if len(books) == 0:
                app.send_message(message.chat.id,f"__Open Library : No results found__", reply_to_message_id=message.id)
            else:
                msg = app.send_photo(message.chat.id, books[0]["cover"],
                    openlibrary.getOpenText(books), reply_to_message_id=message.id, reply_markup=getButtonsIA(books))
                storedata(msg.id,books,"openlib")
        
        # scihub
        elif data[0] == "scihub":
            books = scihub.getSciPubs(search)
            if len(books) == 0:
                app.send_message(message.chat.id,f"__SciHub : No results found__", reply_to_message_id=message.id)
            else:
                try: 
                    msg = app.send_photo(message.chat.id, books[0]["url"],
                    scihub.getSciText(books), reply_to_message_id=message.id, reply_markup=getButtons())
                except:
                    msg = app.send_photo(message.chat.id, noimage,
                    scihub.getSciText(books), reply_to_message_id=message.id, reply_markup=getButtons())
                storedata(msg.id,books,"scihub")

        # end
        return

    # check for validity
    books, website = getdata(call.message.id)
    if books == Null and website == Null: return
    if books == None:
        app.edit_message_media(call.message.chat.id, call.message.id, InputMediaPhoto(wrongimage, "__Out of Date, Search Again__"))
        return

    if call.data[0] == "D": removedata(call.message.id)
    downloded = False

    # pdfdrive
    if website == "pdfdrive":
        downloded = pdfdrive.handlePdfdrive(app,call,books)

    # librarygenesis
    elif website == "librarygenesis":
        downloded = libgen.handleLibGen(app,call,books)
    
    # annas
    elif website == "annas":
        downloded = annas.handleAnnas(app,call,books)
    
    # hunter
    elif website == "hunter":
        downloded = hunter.handleHunt(app,call,books)

    # zlibraray
    elif website == "zlib":
        downloded = zlibrary.handleZlib(Z,app,call,books)
        if call.data[0] == "D": loopZ()
    
    # open lib
    elif website == "openlib":
        downloded = openlibrary.handleOpen(iaemail, iapass, app,call, books)
    
    # scihub
    elif website == "scihub":
        downloded = scihub.handleSchiHub(app,call,books)

    # if downloded: 
    #     removedata(call.message.id)

# infinty polling
app.run()
