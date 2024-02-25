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
        await message.answer('Привет')
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
    await message.answer('''Привет, я GameBot.Я помогу тебе выбрать игру,которая запомнится тебе надолго. 
Для ознакомления с командами пропишите или нажмите на /help''')
@dp.message(F.text.lower() == 'кто тебя создал?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но имя этого гения - Вильдан ')
@dp.message(F.text.lower() == 'кем ты был создан?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но имя этого гения - Вильдан ')
@dp.message(F.text.lower() == 'кем ты создан?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но имя этого гения - Вильдан ')
@dp.message(F.text.lower() == 'кем ты порождён?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но имя этого гения - Вильдан ')
@dp.message(F.text.lower() == 'откуда ты взялся?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но создал гений - Вильдан ')
@dp.message(F.text.lower() == 'как ты появился?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но создал гений - Вильдан ')
@dp.message(F.text.lower() == 'кто тебя породил?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но имя этого гения - Вильдан ')
@dp.message(F.text.lower() == 'как ты появился на свет?')
async def cmd_start(message:types.Message):
    await message.answer('К сожалению это секретная информация.Но создал гений - Вильдан ')
@dp.message(F.text.lower() == 'как тебя зовут?')
async def cmd_start(message:types.Message):
    await message.answer('Меня зовут - GameBot. ')
@dp.message(F.text.lower() == 'как тебя звать?')
async def cmd_start(message:types.Message):
    await message.answer('Меня зовут - GameBot. ')
@dp.message(F.text.lower() == 'звать тебя как?')
async def cmd_start(message:types.Message):
    await message.answer('Меня зовут - GameBot. ')
@dp.message(F.text.lower() == 'что делаешь?')
async def cmd_start(message:types.Message):
    await message.answer('Работаю ')
@dp.message(F.text.lower() == 'на каком языке ты написан?')
async def cmd_start(message: types.Message):
    await message.answer(' <b>Python</b> ',parsemode=ParseMode.HTML)
@dp.message(F.text.lower() == 'на каком языке программирования ты написан?')
async def cmd_start(message: types.Message):
    await message.answer(' <b>Python</b> ',parsemode=ParseMode.HTML)
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
    await message.answer('Список лучших игр:')
    image = FSInputFile('assassins-creed.jpeg')
    await message.answer_photo(image, caption="""
    1. Серия игр Assassin’s Creed. 
Медиафраншиза компании Ubisoft, основанная на серии компьютерных игр. Первая игра вышла в 2007 году, последняя - Assassin’s Creed Mirage - 5 октября 2023 года. Большинство частей франшизы являются играми в жанре приключенческого боевика с открытым миром, где особое внимание уделяется скрытому перемещению и паркуру. """)
    image = FSInputFile('3.jpeg')
    await message.answer_photo(image, caption="""2. Серия игр Outlast. 
Outlast - это видеоигра в жанре ужасов на выживание от первого лица 2013 года, разработанная и изданная компанией Red Barrels. Игра вращается вокруг независимого журналиста-расследователя Майлза Апшура, который решает провести расследование в отдаленной психиатрической больнице под названием Mount Massive Asylum, расположенной глубоко в горах округа Лейк, штат Колорадо.(Первая часть Outlast,помимо неё есть ещё 3 части игры...)""")
    image = FSInputFile('4.jpeg')
    await message.answer_photo(image, caption="""3. Серия игр Grand Theft Auto (GTA).
Серия игр Grand Theft Auto (GTA) — это серия компьютерных игр в жанре action-adventure, созданная и разрабатываемая британской компанией Rockstar North и выпускаемая компанией Rockstar Games.""")
    image = FSInputFile('5.jpg')
    await message.answer_photo(image, caption="""4. Серия игр Forza Horizon.
Forza Horizon — аркадный спин-офф серии гоночных симуляторов Forza Motorsport. Аркадный, но не менее захватывающий: каждая игра линейки посвящена масштабному гоночному фестивалю, и увлечет игрока атмосферой праздника, огромным выбором автомобилей и гибким балансом геймплея между весельем и реализмом.""")
    image = FSInputFile('mine.png')
    await message.answer_photo(image, caption="""5. Minecraft.
Minecraft - самая продаваемая видеоигра в истории, с более чем 238 миллионами проданных копий и почти 140 миллионами активных игроков в месяц по состоянию на 2021 год.
В Minecraft игроки исследуют блочный, процедурно сгенерированный трехмерный мир с практически бесконечной местностью и могут находить и добывать сырье, создавать инструменты и предметы, а также строить сооружения, земляные работы и машины.""")
@dp.message(Command('hgames'))
async def  cmd_start(message:types.Message):
    await message.answer('Список страшных игр от которых кровь стынет в жилах:')



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
