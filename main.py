import os
import telebot

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Olá! O teu bot de ofertas da Shopee está ativo!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    texto = message.text
    if "shopee" in texto.lower():
        resposta = f"🛒 **Oferta Shopee Encontrada!**\n\nLink do produto: {texto}"
        bot.reply_to(message, resposta, parse_mode="Markdown")
    else:
        bot.reply_to(message, "Envia um link da Shopee para eu formatar.")

print("Bot iniciado com sucesso...")
bot.infinity_polling()
