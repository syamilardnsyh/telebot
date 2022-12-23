import asyncio
import openai
from telebot.async_telebot import AsyncTeleBot


# masukin API KEY dan token
openai.api_key = "API KEY OPENAI"
bot = AsyncTeleBot ('TOKEN BOT TELEGRAM')

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hallo salam kenal dengan saya Kieth\
""")
    await bot.reply_to(message, """\
/menu""")
@bot.message_handler(commands=['help'])
async def send_to(message):
    await bot.reply_to(message, """\
Ada yang bisa Kieth bantu?\
""")
@bot.message_handler(commands=['menu'])
async def send_to(message):
    await bot.reply_to(message, '\
MENU wizKiethBOT \n1. /start \n2. /help \n3. /infopromo '
)
@bot.message_handler(commands=['infopromo'])
async def send_to(message):
    await bot.reply_to(message, """\
Cek promo di t.me/yukspill\
""")
    
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])


asyncio.run(bot.polling())