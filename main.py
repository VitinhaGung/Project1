import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

# Включаем логирование, чтобы не пропустить важные сообщения


logging.basicConfig(level=logging.INFO)
#Объект бота
bot = Bot(token="6902830346:AAFvRnFF9kU2G4Jo0ZKGgt9fEpwpljImk64")

dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message, command:CommandObject):
    if command.args is None:
        await message.answer('Приветсвтую')
        return
    else:
        await message.answer(f"Привет,{command.args}")
        return
@dp.message(Command("Monday"))
async def cmd_start(message: types.Message):
    await message.answer("1.Алгебра\n2.Физика\n3.Английский",parsemode=ParseMode.MARKDOWN_V2)
@dp.message(Command("tuesday"))
async def cmd_start(message: types.Message):
    await message.answer("1.Алгебра\n2.Химия\n3.Русский язык")
@dp.message(Command("Wednesday"))
async def cmd_start(message: types.Message):
    await message.answer("1.Русский \n2.Русский\n3.Английский")
@dp.message(Command("Thursday"))
async def cmd_start(message: types.Message):
    await message.answer("1.Основы безопасности жизнедеятельности\n2.Геометрия\n3.История+Общество")
@dp.message(Command("Friday"))
async def cmd_start(message: types.Message):
    await message.answer("1.Алгебра\n2.Литература\n3.Химия")
@dp.message(Command("Saturday"))
async def cmd_start(message: types.Message):
    await message.answer("1.Алгебра\n2.Информатика\n3.Физическая культура")
# @dp.message(F.text)
# async def cmd(message):
#     if message.text=='Привет':
#         await message.answer("Привет!")
@dp.message(F.text.lower() == 'как дела?')
async def cmd_start(message:types.Message):
    await message.answer('У меня всё всегда хорошо,надеюсь и у Вас тоже.')
@dp.message(F.text.lower() == 'привет')
async def cmd_start(message:types.Message):
    await message.answer('Привет, я GameBot.Я помогу тебе выбрать игру,которая запомнится тебе надолго.')
@dp.message(F.text.lower() == 'кто тебя создал?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация. ')
@dp.message(F.text.lower() == 'на каком языке ты написан?')
async def cmd_start(message: types.Message):
    await message.answer(' <b> Python </b> ',parsemode=ParseMode.HTML)
@dp.message(Command('image'))
async def cmd_start(message:types.Message, imagebot=None):
    imagebot = FSInputFile('1.jpg')
    await message.answer_photo(imagebot,caption="Фото")
@dp.message(Command('image_group'))
async def cmd(message:types.Message):
    albom_builder=MediaGroupBuilder(caption="Фото")
    imagebot=FSInputFile('1.jpg')
    imagebot2 = FSInputFile('1.jpg')
    albom_builder.add_photo(media=imagebot)
    albom_builder.add_photo(media=imagebot2)
    await message.answer_media_group(media=albom_builder.build())
@dp.message(Command("help"))
async def cmd_start(message:types.Message):
    await message.answer('В этом разделе вы ознакомитесь с командами бота: \n /igames - Здесь приведён список игр в которые ты должен поиграть! \n /hgames - Здесь приведён список самых страшных игр... \n /sgames - Здесь приведён список лучших шутеров. \n /simgames - Здесь приведён список лучших симуляторов. \n /fgames - Здесь приведён список лучших файтинг игр. \n /stgames - Здесь приведён список лучший стратегических игр. \n /rgames - Здесь приведён список лучших гоночных игр. \n /game - Поиск игр по заданным вами параметрам (найдём для Вас незабываемую игру.) ')

@dp.message(F.text.lower() == 'помощь')
async def cmd_start(message:types.Message):
    await message.answer('Введите команду:/help')
@dp.message(F.text.lower() == 'помогите')
async def cmd_start(message:types.Message):
    await message.answer('Введите команду:/help')
@dp.message(F.text.lower() == 'help')
async def cmd_start(message:types.Message):
    await message.answer('Введите команду:/help')
@dp.message(F.text.lower() == 'хелп')
async def cmd_start(message:types.Message):
    await message.answer('Введите команду:/help')
@dp.message(Command('igames'))
async def cmd_start(message:types.Message):
    image = FSInputFile('2.jpeg')
    await message.answer_photo(image, caption="""Список лучших игр:
    1. Игры Assassin's creed Black Flag и Assassin's creed II""")
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
