from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# board = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("майнкрафт"), KeyboardButton("скачать майнкрафт"))
#
#
# board2 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton("Menu", callback_data="menu")]])
# board2.add(InlineKeyboardButton("Bot_rules", callback_data="rules"))
#
# board3 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton("Мобильні телефони", callback_data="телефони"),
#      InlineKeyboardButton("Рюкзаки", callback_data="рюкзаки")]])
# board3.add(InlineKeyboardButton("Игровие пк", callback_data="игровие пк"), InlineKeyboardButton("Приставки", callback_data="приставки"))

#
# book = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton("books", callback_data="my_books"),
#      InlineKeyboardButton("Обратная связь", callback_data="Feedback")]])

book = InlineKeyboardMarkup().add(InlineKeyboardButton(text="books", callback_data="my_books"))