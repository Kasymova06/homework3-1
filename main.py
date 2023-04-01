from aiogram import Bot, Dispatcher, types, executor
import config
from random import randint
bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.")
    await message.answer(f"Используйте /startran для начала рандома.")

@dp.message_handler(commands="startran")
async def game(message:types.Message):
    await message.answer("Введите любое число от 1 до 3.")

@dp.message_handler(regexp=r"^[1-9]|10$")
async def randomizr(message:types.Message):
    integ = randint(1, 3)
    user_int = int(message.text)
    await message.reply("Правильно вы отгадали")
    





executor.start_polling(dp)