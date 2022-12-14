from requests import get
from bs4 import BeautifulSoup
from pyrogram.types import InputMediaPhoto, InputMediaDocument, CallbackQuery
from pyrogram import Client
from buttons import getButtons
from os import remove


def getAnnasBooks(searchbook):
    params = {'q': searchbook}
    response = get('https://annas-archive.org/search', params=params)
    soups = BeautifulSoup(response.content,"html.parser")
    soups = soups.findAll("div",class_="mb-4")[-1].findAll("div",class_="h-[125]")
    books = []

    for soup in soups:
        soup = BeautifulSoup(str(soup).replace("<!--","").replace("-->",""),"html.parser")
        info = soup.find("div",class_="relative top-[-1] pl-4 grow overflow-hidden")
        desc = info.find("div",class_="truncate text-xs text-gray-500").text.split(",")
        book = {
                "link" : 'https://annas-archive.org' + soup.find("a").get("href"),
                "cover" : soup.find("img").get("src"),
                "title" : info.find("div",class_="truncate text-xl font-bold").text,
                "publisher" : info.find("div",class_="truncate text-sm").text,
                "author" : info.find("div",class_="truncate italic").text,
                "language" : desc[0],
                "extension" : desc[1][1:],
                "size" : desc[2][1:],
                "filename" : desc[3].replace('"',"")[1:]
            }
        books.append(book)

    return books


def getDownLinks(book):
    res = get(book["link"])
    soup = BeautifulSoup(res.content,"html.parser")
    soup = soup.find("div",class_="mb-4 p-6 overflow-hidden bg-[#0000000d] break-words").findAll("a")
    links = []
    for ele in soup:
        link = ele.get("href")
        if "http://lib" not in link:
            links.append(link)

    return links


def getAnnasText(books,choose=0):
    return f'**{books[choose]["title"]}**\n\n__Author: {books[choose]["author"]}\nPublisher: {books[choose]["publisher"]}\nSize: {books[choose]["size"]}\nLanguage: {books[choose]["language"]}\nExtension: {books[choose]["extension"]}__'


def handleAnnas(app:Client,call:CallbackQuery,books):

    # download
        if call.data[0] == "D":
            choose = int(call.data.replace("D",""))
            app.edit_message_text(call.message.chat.id, call.message.id, "__Downloading__")
            links = getDownLinks(books[choose])

            i = 0
            while i<len(links):
                print(links[i])
                res = get(links[i])
                if res.status_code == 200: break
                else: i += 1
            
            if i == len(books):
                app.edit_message_text(call.message.chat.id, call.message.id, "__Failed__")
                return 

            filename = f"{books[choose]['title']}"
            filename = "".join( x for x in filename if (x.isalnum() or x in "_ ")) + f".{books[choose]['extension']}"
            with open(filename, "wb") as file:
                file.write(res.content)

            res = get(books[choose]["cover"])
            thumbfile = f"{books[choose]['title']}"
            thumbfile = "".join( x for x in thumbfile if (x.isalnum() or x in "_ ")) + ".jpg"
            with open(thumbfile, "wb") as file:
                file.write(res.content)
                
            app.edit_message_text(call.message.chat.id, call.message.id, "__Uploading__")
            app.edit_message_media(call.message.chat.id, call.message.id, InputMediaDocument(filename, thumb=thumbfile, caption=f"**{books[choose]['title']}**"))
            remove(filename)
            remove(thumbfile)
            return

        #  next
        choose = int(call.data) % len(books)
        app.edit_message_media(call.message.chat.id, call.message.id,
            InputMediaPhoto(books[choose]["cover"],getAnnasText(books,choose)),
            reply_markup=getButtons(choose))



