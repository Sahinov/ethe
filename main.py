import telebot

from tradingview_ta import TA_Handler, Interval, Exchange

eth = TA_Handler(
    symbol="ETHUSD",
    screener="crypto",
    exchange="binance",
    interval=Interval.INTERVAL_1_MINUTE,
)

result = eth.get_analysis()

bot = telebot.TeleBot('5130280422:AAE9HHUFRVHYattkLv1Zw5ixaIWzAA1-Zgw')
@bot.message_handler(commands=['eth'])
def eth(message):
    bot.send_message(message.chat.id, 'Цена Ethereum: ')
    bot.send_message(message.chat.id, result.indicators['open'])
bot.polling()
