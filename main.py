import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.reply_to_message:
        pokemon_1 = Pokemon.pokemons[message.from_user.username]
        pokemon_2 = Pokemon.pokemons[message.reply_to_message.from_user.username]
        result = pokemon_1.attack(pokemon_2)
        bot.send_message(message.chat.id, result)
    else:
        bot.reply_to(message, "Выбери противника (ответь на другое сообщение командой /attack)")


bot.infinity_polling(none_stop=True)

