import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram import F
# Включаем логирование, чтобы не пропустить важные сообщения


logging.basicConfig(level=logging.INFO)
#Объект бота
bot = Bot(token="6902830346:AAFvRnFF9kU2G4Jo0ZKGgt9fEpwpljImk64")

dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
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
@dp.message(F.text)
async def cmd(message):
    if message.text=='Привет':
        await message.answer("Привет!")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
