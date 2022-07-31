import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5524717837:AAG1Ytoqc8s-zHT-1pzkTYuayXVTr1GWuFI'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  await message.reply(f"Botga xush kelibsiz,\nMalumotlaringiz:\n\nIsm-Familiya: {message.from_user.first_name}\nUsername: @{message.from_user.username}\n\nID: {message.from_user.id}\nFamiliya: {message.from_user.last_name}\n")
URL = 'https://docs.aiogram.dev/en/dev-2.x/_static/logo.png'
@dp.message_handler(commands=['image', 'img'])
async def send_Photo(message: types.Message):
  await bot.send_Photo(message.chat.id,types.InputFile.from_url(URL))

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
