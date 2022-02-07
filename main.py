from platforms import youtube
import information

# from selenium import webdriver


def games_name_get():
    with open('data/games_name', 'r', encoding='utf-8') as file:
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
            break
        elif command == '2':
            start()
            break
        else:
            print('Команда не распознана, попробуйте ещё раз')
    print()


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

        # name = 'Apex Legends'

    print(f"Выберите платформу на которой искать стримы по игре '{name}':")
    print("   1. YouTube")
    print("   2. Facebook Gaming")
    print("   3. Искать везде")
    print()
    print("   0. Вернуться назад")
    print()

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
