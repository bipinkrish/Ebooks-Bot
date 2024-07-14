from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def getExtButton(link):
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text='External Link', url=link),
        ]])


def getButtons(choose=0):
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text='⬅️', callback_data=str(choose-1)),
            InlineKeyboardButton(text='✅', callback_data=f'D{choose}'),
            InlineKeyboardButton(text='➡️', callback_data=str(choose+1))
        ]])


def getButtonsIA(books, choose=0,):
    if isinstance(books[choose]['ia'], str):
        return InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(text='⬅️', callback_data=str(choose-1)),
                InlineKeyboardButton(text='✅', callback_data=f'D{choose}'),
                InlineKeyboardButton(text='➡️', callback_data=str(choose+1))
            ]])

    temp = []
    for i in range(len(books[choose]['ia'])):
        temp.append(InlineKeyboardButton(
            text=f'{i+1}', callback_data=f'D{choose},{i}'))

    main = [[
            InlineKeyboardButton(text='⬅️', callback_data=str(choose-1)),
            InlineKeyboardButton(text='➡️', callback_data=str(choose+1))
            ]]
    for i in range(0, len(temp), 3):
        main.append(temp[i:i+3])

    return InlineKeyboardMarkup(main)


def getSrc():
    return InlineKeyboardMarkup(
        [   
            [InlineKeyboardButton(text='Source Code 🌐', url="https://github.com/bipinkrish/Ebooks-Bot")],
            [InlineKeyboardButton(text='Donate Me 💸', url="https://github.com/sponsors/bipinkrish")],
        ]
    )
