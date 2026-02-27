import telebot
from telethon import TelegramClient
import asyncio

# بياناتك المسجلة والمحمية
api_id = 39129538
api_hash = '902fb56fc008dcd0bde80ab6a05a828f'
BOT_TOKEN = '8648508756:AAHL8JumdSLiqEywFlglfdKNTGIfGWL5EHI'
TARGET_BOT_ID = 8579695015

bot = telebot.TeleBot(BOT_TOKEN)
client = TelegramClient('session', api_id, api_hash)

@bot.message_handler(commands=['reset'])
def handle_reset(message):
    msg_parts = message.text.split()
    if len(msg_parts) > 1:
        key = msg_parts[1]
        async def send_via_user():
            await client.send_message(TARGET_BOT_ID, f"/reset {key}")
            bot.reply_to(message, f"✅ تم توجيه الطلب للمفتاح: {key}")
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(client.start())
        loop.run_until_complete(send_via_user())
    else:
        bot.reply_to(message, "⚠️ أرسل الكود بعد الأمر، مثال: /reset 123")

if __name__ == "__main__":
    bot.polling(none_stop=True)
