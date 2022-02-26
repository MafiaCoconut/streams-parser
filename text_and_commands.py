import main1


def main_menu():
    print('Выберите команду:')
    print("   1. Работа с базой данных")
    print("   2. Получение информации о трасляциях")
    print("   3. Получение списка названий всех игр")
    print()
    print("   9. Рекомендации")
    print("   0. Выход")
    print()


def recommendations():
    print("Перед началом работы, рекомендуется обновить базу данных в пункте №1 на стартовом экране.")
    print("Далее рекомендуется, в ситуации когда вы не помните полное название игры, запросить список названий игр.")
    print("Если программы пишет что игры нет в списке, то возможно стримы по игре сейчас находятся не в топ 50 самых "
          "популярных играх.")
    print("Приятного использования программы!!!")
    print()
    main1.start()


def choosing_a_platform(name):
    print(f"Выберите платформу на которой искать стримы по игре '{name}':")
    print("   1. YouTube")
    print("   2. Facebook Gaming")
    print("   3. Искать везде")
    print()
    print("   0. Вернуться назад")
    print()