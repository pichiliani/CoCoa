# NOTA: instalar com o pip install twx.botapi
# Mais info do projeto em https://github.com/datamachine/twx.botapi
from twx.botapi import TelegramBot, ReplyKeyboardMarkup


bot = TelegramBot('438194506:AAGYIHrARnrnVU1Ev9UOrYA7hdvOXFW0g-Y')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""
# No caso para o Mauro
user_id = int(315613935)

result = bot.send_message(user_id, 'Msg da Dragon').wait()
print(result)

"""
Get updates sent to the bot
"""
#updates = bot.get_updates().wait()
#for update in updates:
#    print(update)

"""
Use a custom keyboard
"""
#keyboard = [
#    ['7', '8', '9'],
#    ['4', '5', '6'],
#    ['1', '2', '3'],
#         ['0']
#]
#reply_markup = ReplyKeyboardMarkup.create(keyboard)

#bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()