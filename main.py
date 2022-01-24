import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3

import os
import re
import time
from bs4 import BeautifulSoup
import youtube
import information

# from selenium import webdriver


def games_name_get():
    with open('data/games_name', 'r', encoding='utf-8') as file:
        games_name = list(file.read().split(';'))
    return games_name


def working_with_databases():
    print('Обновить базу данных?')
    print('1. Да   /   2. Нет')
    while True:
        command = input()
        print()
        if command == '1':
            youtube.update_data()
            print('База данных обновлена')
            print()
            start()
            break
        elif command == '2':
            start()
            break
        else:
            print('Команда не распознана, попробуйте ещё раз')
    print()


def working_with_youtube(data_youtube, name):
    print("Трансляции YouTube:")
    print()
    for i in range(len(data_youtube[name])):
        print(f'Трансляция №{i+1}')
        print(f'   Название трансляции: {data_youtube[name][i]["video title"]}')
        print(f'   Автор: {data_youtube[name][i]["channel name"]}')
        print(f'   Ссылка на  трансляцию: {data_youtube[name][i]["url"]}')
        print()
    working_with_streams()


def working_with_streams():
    print("Выберите платформу на которой искать стримы:")
    print("   1. YouTube")
    print("   2. Facebook Gaming")
    print("   3. Искать везде")
    print()
    print("   0. Вернуться назад")

    com = -1
    while True:
        com = input("Введите номер команды: ")
        if com == "1":
            break
        elif com == "2":
            break
        elif com == "3":
            break
        elif com == "0":
            start()


    data_youtube = youtube.data_get()
    # data_facebook_gaming = data_get()

    name = input('Введите название игры:')
    while True:
        if name == 'exit':
            start()
        elif name in data_youtube:
            break
        else:
            print('Такой игры нет, попробуйте ещё раз или наберите "exit"')
            print()
        name = input('Введите название игры:')
        # name = 'Apex Legends'

    working_with_youtube(data_youtube, name)


def working_with_games_name():
    games_name = games_name_get()
    print(f'Количество названий игр: {len(games_name)}')
    for i in range(0, len(games_name), 3):
        for j in range(3):
            try:
                print(games_name[i+j], end='; ')
            except:
                break
        print()
    print()
    start()


def recommendations():
    print("Перед началом работы, рекомендуется обновить базу данных в пункте №1 на стартовом экране.")
    print("Далее рекомендуется, в ситуации когда вы не помните полное название игры, запросить список названий игр.")
    print("Если программы пишет что игры нет в списке, то возможно стримы по игре сейчас находятся не в топ 50 самых "
          "популярных играх.")
    print("Приятного использования программы!!!")
    print()
    start()


def start():
    print('Выберите команду:')
    print("   1. Работа с базой данных")
    print("   2. Получение информации о трасляциях")
    print("   3. Получение списка названий всех игр")
    print()
    print("   9. Рекомендации")
    print("   0. Выход")
    print()

    while True:
        command = input("Введите номер команды: ")
        if command == '1':
            print()
            working_with_databases()
            break
        elif command == '2':
            print()
            working_with_streams()
            break
        elif command == '3':
            print()
            working_with_games_name()
            break
        elif command == '9':
            print()
            recommendations()
            break
        elif command == '0':
            break
        else:
            print("Команда не распознана, попробуйте ещё раз")
            print()


def main():
    print('Добро пожаловать в парсер онлайн трансляций на youtube')
    start()

    """
    pyautogui.hotkey('command', 'l')
    """


if __name__ == '__main__':
    main()
