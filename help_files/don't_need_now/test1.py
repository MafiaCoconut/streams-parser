import youtube
from help_files import information
import text_and_commands


# from selenium import webdriver


def games_name_get():
    x = []
    with open('../names_of_games', 'r', encoding='utf-8') as file:
        games_name = list(file.read().split(';'))
    return games_name



def working_with_databases():
    print('Обновить базу данных?')
    print(f'Последнее изменение {information.database_time["youtube"]}')
    print('1. Да   /   2. Нет')
    while True:
        command = input()
        print()
        if command == '1':
            youtube.update_data()
            print('База данных обновлена')
            print()
            start()
        elif command == '2':
            start()
        else:
            print('Команда не распознана, попробуйте ещё раз')


def working_with_streams():
    games_name = games_name_get()
    name = input('Введите название игры: ')
    while True:
        print()
        if name == '0':
            start()
        elif name in games_name:
            break
        else:
            print('Такой игры нет, попробуйте ещё раз или наберите "0"')
            print()
        name = input('Введите название игры: ')

    text_and_commands.choosing_a_platform(name)

    while True:
        com = input("Введите номер команды: ")
        print()
        if com == "1":
            youtube.streams(name)
        elif com == "2":
            start()
        elif com == "3":
            start()
        elif com == "0":
            start()


def working_with_games_name():
    games_name = games_name_get()
    print(f'Количество названий игр: {len(games_name)}')
    for i in range(0, len(games_name), 3):
        for j in range(3):
            try:
                print(games_name[i + j], end='; ')
            except:
                break
        print()
    print()
    start()


def start():
    text_and_commands.main_menu()

    while True:
        command = input("Введите номер команды: ")
        print()
        if command == '1':
            working_with_databases()
        elif command == '2':
            working_with_streams()
        elif command == '3':
            working_with_games_name()
        elif command == '9':
            text_and_commands.recommendations()
        elif command == '0':
            exit()
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
