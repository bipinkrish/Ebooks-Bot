from os import remove
from requests import get
from bs4 import BeautifulSoup
from pyrogram.types import InputMediaPhoto, InputMediaDocument, CallbackQuery
from pyrogram import Client
from buttons import getButtons

class searchedbookinfo:
    title: str
    link: str
    id: str
    coverlink: str
    year: str
    size: str
    downloads: str
    pages: str


def getpage(searchterm):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.pdfdrive.com/',
        'Alt-Used': 'www.pdfdrive.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1'
              }
    
    params = { 'q': searchterm, 'pagecount': '', 'pubyear': '', 'searchin': '', 'em': '1', 'more': 'true' }

    response = get('https://www.pdfdrive.com/search', params=params,  headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    #TotalResults = soup.find("div",class_="dialog-main").find("div", id="result-found").findAll("strong")[0].string
    #TimeTaken = soup.find("div",class_="dialog-main").find("div", id="result-found").findAll("strong")[1].string

    soup = soup.find("div", class_="files-new").findAll("li")
    books = []
    for ele in soup:

        try:
            book = searchedbookinfo()
            book.id = ele.find("a").get("data-id")
            book.link = "https://www.pdfdrive.com" + ele.find("a").get("href")
            book.coverlink = ele.find("a").find("img").get("data-original") #src
            title = ""
            for word in ele.find("a",class_="ai-search").findAll("b"):
                title = title + word.string + " "
            if title == "":
                book.title = ele.find("a",class_="ai-search").find("h2").string
            else:
                book.title = title
            book.pages = ele.find("div",class_="file-info").find("span",class_="fi-pagecount").string.split(" ")[0]
            book.year = ele.find("div",class_="file-info").find("span",class_="fi-year").string
            book.size = ele.find("div",class_="file-info").find("span",class_="fi-size").string
            book.downloads = ele.find("div",class_="file-info").find("span",class_="fi-hit").string.string.split(" ")[0]
            books.append(book)

        except:
            pass

    return books


def getdownlink(book):

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': book.link,
    'Alt-Used': 'www.pdfdrive.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',

    }

    url = book.link.replace(f'e{book.id}',f"d{book.id}")
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text,"html.parser").findAll("script")[7].get_text()
    
    temp = soup.split("{")
    for ele in temp:
        if "id" in ele and "session" in ele:
            id = ele.split("'")[1]
            sess = ele.split("'")[3]

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Alt-Used': 'www.pdfdrive.com',
        'Connection': 'keep-alive',
        'Referer': url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
            }

    params = { 'id': id, 'session': sess,}

    response = get('https://www.pdfdrive.com/ebook/broken', params=params,  headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    res = soup.find("a").get('href')

    if "http" in res:
        durl = res
    else:
        durl = f'https://www.pdfdrive.com/download.pdf?id={id}&h={sess}&u=cache&ext=pdf' # or "https://www.pdfdrive.com" + res
    
    print(durl)
    return durl


def getPdfText(books,choose=0):
    return f'**{books[choose].title}**\n\n__Year: {books[choose].year}\nSize: {books[choose].size}\nPages: {books[choose].pages}\nDownloads: {books[choose].downloads}__'

def handlePdfdrive(app:Client,call:CallbackQuery,books:list[searchedbookinfo]):

    # download
        if call.data[0] == "D":
            choose = int(call.data.replace("D",""))
            app.edit_message_text(call.message.chat.id, call.message.id, "__Downloading__")
            durl = getdownlink(books[choose])
            res = get(durl)
            filename = f"{books[choose].title}"
            filename = "".join( x for x in filename if (x.isalnum() or x in "_ ")) + ".pdf"
            with open(filename, "wb") as file:
                file.write(res.content)
            res = get(books[choose].coverlink)
            thumbfile = f"{books[choose].title}"
            thumbfile = "".join( x for x in thumbfile if (x.isalnum() or x in "_ ")) + ".jpg"
            with open(thumbfile, "wb") as file:
                file.write(res.content)
            app.edit_message_text(call.message.chat.id, call.message.id, "__Uploading__")
            app.edit_message_media(call.message.chat.id, call.message.id, InputMediaDocument(filename, thumb=thumbfile, caption=f"**{books[choose].title}**"))
            remove(filename)
            remove(thumbfile)
            return

        #  next
        choose = int(call.data) % len(books)
        try:
            app.edit_message_media(call.message.chat.id, call.message.id,
            InputMediaPhoto(books[choose].link,getPdfText(books,choose)),
            reply_markup=getButtons(choose))
        except:
            app.edit_message_media(call.message.chat.id, call.message.id,
            InputMediaPhoto(books[choose].coverlink,getPdfText(books,choose)),
            reply_markup=getButtons(choose))