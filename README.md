# Ebooks Bot

*This is Ebooks Finder Bot, Just send a name of the Book and It will get you results from [Library Genesis](https://libgen.li/), [Zlibrary](http://z-lib.org/), [OpenLibrary](https://openlibrary.org)/[InternetArchive](https://archive.org/), [SciHub](https://sci-hub.se/), [Anna's Archive](https://annas-archive.org/), [PdfDrive](https://pdfdrive.to) and [eBook-Hunter](https://ebook-hunter.org/) to Telegram*

*Experience the bot at [@eBooooksBot](https://t.me/ebooooksbot)*

---

## Required Variables

- `HASH` Your API Hash from my.telegram.org
- `ID` Your API ID from my.telegram.org
- `TOKEN` Your bot token from @BotFather

## Optional Variables

* for **Zlibrary**

    `REMIX_ID` & `REMIX_KEY` OR `Z_EMAIL` & `Z_PASS`

* for **Zlibrary Multi**

    `ZLIB_MULTI`

    _Below is an eample config, you can use either of the logins combination_

```json
    "ZLIB_MULTI": [
        {
            "email": "xxx@mail.com",
            "password": "ABCDEF"
        },
        {
            "remix_id": 12345678,
            "remix_key": "24jhbf32hj2b3hjb"
        }
    ]
```

* for **OpenLibrary**

    `IA_EMAIL` & `IA_PASS`
