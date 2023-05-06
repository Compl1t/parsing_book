from aiogram import types, Dispatcher, Bot, executor
import asyncio
import requests
from bs4 import BeautifulSoup
from key_boards import book
from token import token


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def bot_hello(message: types.Message):
    await message.answer(f"Hello @{message.from_user.username}", reply_markup=book)


@dp.callback_query_handler(text="my_books")
async def books_top(call: types.CallbackQuery):
    # await bot.answer_callback_query(call.id)
    url = "https://book24.ua/ua/catalog/letnee_chtenie_po_shkolnoy_programma/"
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    literatyra = soup.select(".inner_wrap")
    for item in literatyra:
        try:
            name = item.select(".item-title > a > span")[-1].text
            price = item.select(".price_matrix_wrapper > .price")[0].text.strip()
            avtor = item.select(".article_block > .muted > a")[-1].text
            available = item.select(".item-stock > span")[-1].text
            picture = item.find("span", class_="section-gallery-wrapper__item _active").find("img")["data-src"]
            picture2 = "https://book24.ua/" + picture
            await asyncio.sleep(2)
            await call.message.answer_photo(caption=f"<b>{name}</b>\n<i>{price}</i>\n{avtor}", parse_mode="HTML", photo=picture2)
        except Exception as e:
            print("ОШИБКА", e)


# @dp.callback_query_handler(text="my_books")
# async def books_top(call: types.CallbackQuery):
#     url = "https://book24.ua/ua/catalog/letnee_chtenie_po_shkolnoy_programma/"
#     request = requests.get(url)
#     soup = BeautifulSoup(request.text, "html.parser")
#     literatyra = soup.select(".inner_wrap")
#     for item in literatyra:
#         try:
#             name = item.select(".item-title > a > span")[-1].text
#             price = item.select(".price_matrix_wrapper > .price")[0].text.strip()
#             avtor = item.select(".article_block > .muted > a")[-1].text
#             available = item.select(".item-stock > span")[-1].text
#             picture = item.find("span", class_="section-gallery-wrapper__item _active").find("img")["data-src"]
#             picture2 = "https://book24.ua/" + picture
#             await bot.send_photo(call.message.chat.id, picture2,
#                                  caption="<b>" + name + "</b>\n<i>" + price + "\n" + avtor + "</i>\n<a",
#                                  parse_mode="html")
#         except:
#             ValueError()


# @dp.callback_query_handler(text="Feedback")
# async def Back(call: types.CallbackQuery):
#     await call.answer(f"Для сотруднечества по рекламе пишите мне @{call.from_user.username}")


executor.start_polling(dp)



