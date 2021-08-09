import telepot

token = '1468367155:AAH98aaz_oAr2E8erZSHFTxIwUuFBnIPSac'
my_id = -552641621
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")

