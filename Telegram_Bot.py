import telebot
import requests
from datetime import date, timedelta
from telebot import types

BOT_TOKEN = '7736030118:AAFEl1PRJldw3rfPi5WoZLnJ-Z3ef1_vc-g'
OPENWEATHERMAP_API_KEY = 'db09ee5a1c85594cb1bb6f1c49b04d40'

bot = telebot.TeleBot(BOT_TOKEN)


def get_weather(city, date_offset=0):
    requested_date = date.today() + timedelta(days=date_offset)
    timestamp = int(requested_date.strftime("%s"))
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric&dt={timestamp}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        closest_forecast = min(data['list'], key=lambda x: abs(int(x['dt']) - (timestamp + 12 * 3600)))
        temperature = round(closest_forecast['main']['temp'])
        feels_like = round(closest_forecast['main']['feels_like'])
        description = closest_forecast['weather'][0]['description']
        wind_speed = round(closest_forecast['wind']['speed'])
        humidity = closest_forecast['main']['humidity']

        if date_offset == 0:
            return f"Погода в городе {city} сегодня:\n\nТемпература: {temperature}°C\nОщущается как: {feels_like}°C\n{description.capitalize()}\nСкорость ветра: {wind_speed} м/с\nВлажность: {humidity}%"
        else:
            return f"Прогноз погоды на {requested_date.strftime('%d.%m.%Y')} в городе {city}:\n\nТемпература: {temperature}°C\nОщущается как: {feels_like}°C\n{description.capitalize()}\nСкорость ветра: {wind_speed} м/с\nВлажность: {humidity}%"
    else:
        return "Ошибка получения данных о погоде."


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
    itembtn1 = telebot.types.KeyboardButton('Текущая погода')
    itembtn2 = telebot.types.KeyboardButton('Прогноз погоды на завтра')
    itembtn4 = telebot.types.KeyboardButton('Погода на дату')
    markup.add(itembtn1, itembtn2, itembtn4)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Текущая погода')
def current_weather(message):
    bot.send_message(message.chat.id, "Введите название города:")
    bot.register_next_step_handler(message, send_current_weather)


def send_current_weather(message):
    city = message.text
    weather = get_weather(city)
    bot.send_message(message.chat.id, weather)


@bot.message_handler(func=lambda message: message.text == 'Прогноз погоды на завтра')
def tomorrow_weather(message):
    bot.send_message(message.chat.id, "Введите название города:")
    bot.register_next_step_handler(message, send_tomorrow_weather)


def send_tomorrow_weather(message):
    city = message.text
    weather = get_weather(city, date_offset=1)
    bot.send_message(message.chat.id, weather)




@bot.message_handler(func=lambda message: message.text == 'Погода на дату')
def date_weather(message):
    bot.send_message(message.chat.id, "Введите дату в формате ДД.ММ.ГГГГ:")
    bot.register_next_step_handler(message, get_date_weather)


def get_date_weather(message):
    try:
        input_date = message.text.split('.')
        day = int(input_date[0])
        month = int(input_date[1])
        year = int(input_date[2])
        requested_date = date(year, month, day)
        date_offset = (requested_date - date.today()).days
        bot.send_message(message.chat.id, "Введите название города:")
        # Передаем date_offset в send_date_weather
        bot.register_next_step_handler(message, send_date_weather, date_offset)
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Неверный формат даты. Попробуйте снова.")


def send_date_weather(message, date_offset):
    city = message.text
    weather = get_weather(city, date_offset=date_offset)
    bot.send_message(message.chat.id, weather)


bot.polling()
