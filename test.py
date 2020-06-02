def start_handler(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, 'Привіт, скільки вам рочків?')
    bot.register_next_step_handler(msg, askAge)


def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if text.isdigit():
        checkAge(message)
        get_text_messages(message)
    else:
        msg = bot.send_message(chat_id, 'Вік повинен бути числом.')
        bot.register_next_step_handler(msg, askAge)


def checkAge(message):
    chat_id = message.chat.id
    text = message.text
    if int(text) >= 18:
        bot.send_message(chat_id, 'Чудово!')
    else:
        bot.send_message(chat_id, 'Вам повинно бути більше 18 рочків')

def get_text_messages(message):
    chat_id = message.chat.id
    text = message.text
    if int(text) >= 18:
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_volonteer = telebot.types.InlineKeyboardButton(text='Волонтер', callback_data='volonteer', url="https://forms.gle/TEykbjoMVVT96DAZ9")
        keyboard.add(key_volonteer)
        key_client = telebot.types.InlineKeyboardButton(text='Клієнт', callback_data='client')
        keyboard.add(key_client)
        bot.send_message(message.from_user.id, text='Обирай, хто ти:', reply_markup=keyboard)

    else:
        bot.send_message(message.from_user.id, "На жаль, тільки повнолітні можуть працевлаштовуватися та брати тварину з притулку.")

@bot.callback_query_handler(func=lambda call: True)
def client(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_findAnimal = telebot.types.InlineKeyboardButton(text='Я загубив(-ла) тваринку', callback_data='findAnimal')
    keyboard.add(key_findAnimal)
    key_takeAnimal = telebot.types.InlineKeyboardButton(text='Я хочу взяти собі тваринку', callback_data='takeAnimal')
    keyboard.add(key_takeAnimal)
    key_giveAnimal = telebot.types.InlineKeyboardButton(text='Я хочу віддати тваринку', callback_data='giveAnimal')
    keyboard.add(key_giveAnimal)

    bot.send_message(message.from_user.id, text='Чим можемо тобі допомогти?', reply_markup=keyboard)

