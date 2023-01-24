# -*- coding: utf-8 -*-
import re
import sqlite3
import random

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

conn = sqlite3.connect('tst.db')
cur = conn.cursor()
cur.execute('create table if not exists tbl(quest text,answ text)')

commands = {"Привет": "Привет", "привет": "Привет ))",
            "こんにちわ": "Конитива конитива", "Хай": "Hi", "хай": "Hi ))", "Help": "Доступные команды: Погода (город с большой буквы), число(знак)число",
            ";0": ":0", ":0": ":000",
            "как дела": "Вполне не плохо", "как дела?": "Ну вот какие у бота могут быть дела :D", "как дела ?": "Ну вот какие у бота могут быть дела :D",
            "Как дела": "Пока функционирую - значит все хорошо", "Как дела?": "Ну вот какие у бота могут быть дела :D",
            "Как дела ?": "Ну вот какие у бота могут быть дела :D", "я человек": "А я бот .-.", "Погода Москва": '', "Погода Астрахань": '', "Погода СПб": '', "Погода Котельнич": '', "Погода Самара": '', "Погода Тюмень": '', }

def main():
    print("Hello")
    vk_session = vk_api.VkApi(
        token='здесь токен вк бота')

    longpoll = VkBotLongPoll(vk_session, 'здесь id вк бота', wait=1)
    vk = vk_session.get_api()

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print()
            if event.obj.text in commands:
                if event.obj.text == "Погода Москва":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Москва\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))), str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Котельнич":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Kotelnich&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Котельнич\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))), str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода СПб":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Petersburg&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Санкт-Петербург\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))), str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Астрахань":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Astrakhan&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Астрахань\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))), str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Тюмень":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Tyumen&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Тюмень\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))), str(round(int(r.json()['main']['humidity']))))
                    )
                elif event.obj.text == "Погода Самара":
                    r = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?q=Samara&APPID=e718fecef4a70834c41d4a1a688b0dba")
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message="Самара\nТемпература {0} ℃\nСкорость ветра {1} м/с\nВлажность {2}%".format(str(round(int(r.json()['main']['temp'])-273.15, 2)), str(round(int(r.json()['wind']['speed']))), str(round(int(r.json()['main']['humidity']))))
                    )

                else:
                    vk.messages.send(
                        peer_id=event.obj.from_id,
                        random_id=get_random_id(),
                        message=commands[event.obj.text]
                    )
            elif re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)", event.obj.text):
                try:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message=eval(str(re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)", event.obj.text).group(0)))
              	  )
                except:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message='Ошибка'
                	)
            elif re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)", event.obj.text):
                try:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message=eval(str(re.match(r"(\d+)([\+\-\*\/])(\d+)([\+\-\*\/])(\d+)", event.obj.text).group(0)))
              	  )
                except:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message='Ошибка'
                	)
            elif re.match(r"(\d+)([\+\-\*\/])(\d+)", event.obj.text):
                try:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message=eval(str(re.match(r"(\d+)([\+\-\*\/])(\d+)", event.obj.text).group(0)))
              	  )
                except:
                	vk.messages.send(
                 	   peer_id=event.obj.from_id,
               	     random_id=get_random_id(),
              	      message='Ошибка'
                	)

            else:
                vk.messages.send(
                    peer_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message="Команда не найдена"
                )

        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print('Новое сообщение:')

            print('От меня для: ', end='')

            print(event.obj.peer_id)

            print('Текст:', event.obj.text)
            print()

        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')

            print(event.obj.from_id, end=' ')

            print('для ', end='')

            print(event.obj.to_id)
            print()

        elif event.type == VkBotEventType.GROUP_JOIN:
            print(event.obj.user_id, end=' ')

            print('Вступил в группу!')
            print()

        elif event.type == VkBotEventType.GROUP_LEAVE:
            print(event.obj.user_id, end=' ')

            print('Покинул группу!')
            print()

        else:
            print(event.type)
            print()


if __name__ == '__main__':
    main()
