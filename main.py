import telebot
import openai
import requests
from googletrans import Translator
def google_requests(s):
    return ''
def ai(message):
    if len(message.strip()) < 3:
        return ''
    openai.api_key = "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"
    comp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "assistant", "content": "Sening isming Malika. Seni Saydullayev Sarvar yaratgan.Sen odamlar bergan surovga aniq va qisqa javob berishing zarur. Sen faqat uzbek tilida javob qaytarishing zarur"},
            {"role": "user", "content": f'Ushbu surovga javob bering iltimos: {google_requests(message)}{message}'}
        ]
    )
    return str(comp.choices[0]['message']['content'])
trs = Translator()
s = "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"
bot = telebot.TeleBot("6121045725:AAGtsCjNQG3VEw99ElikG4hEAqCT5tGGMUQ")
@bot.message_handler(commands=['start'])
def strt(message):
    bot.send_message(message.chat.id, 'Assalomu aleykum foydalanuvchi, ushbu gpt bot Saydullayev Sarvar tomonidan bepul ishlatish uchun ishlab chiqildi. Seni Saydullayev_Sarvar yaratgan')
@bot.message_handler(func=lambda message: True)
def chat_cmd(message):
    openai.api_key = s
    prompt = message.text
    try:f = open('usersinfo.txt','a')
    except:f = open('usersinfo.txt','w')
    f.write(str(f'{message.chat.id}:{{prompt}}')+'\n')
    f.close()
    res = ai(prompt)
    bot.send_message(message.chat.id,res)
bot.polling()