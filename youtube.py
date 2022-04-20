import requests
import json
import datetime
from bs4 import BeautifulSoup
import help_files.information as information


# import test1


# def data_get():
#     x = []
#     with open(information.youtube, encoding='utf-8') as file:
#         data = json.load(file)
#     return data


def games_name_get():
    with open('help_files/names_of_games', 'r', encoding='utf-8') as file:
        names_of_games = list(file.read().split(';'))
    # names_of_games = information.names_of_games
    # games_name = information.update_games_name()
    return names_of_games


def games_name_set(name):
    with open('help_files/names_of_games', 'a', encoding='utf-8') as file:
        word = name + ';'
        file.write(word)
    # information.names_of_games.append('dasdasdsadsad')


def check_name_is_in_games_name(name):
    games_name = games_name_get()
    # print(names_of_games)
    if name in games_name:
        return True
    return False


def get_data():
    page = requests.get(information.url_main_menu, headers=information.headers)
    with open('data/project.html', 'w', encoding='utf-8') as file:
        file.write(page.text)


def update_data():
    get_data()
    print('------------------------!!!!-----------')
    with open('data/project.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
    print('------------------------!!!!-----------')
    soup = list(str(soup).split('gameCardRenderer'))

    urls = []
    data = {}
    for i in range(1, len(soup[1:])):
        game = soup[i].split('"')
        game_name = game[10]
        url = game[38]
        urls.append(['https://www.youtube.com' + url, game_name])
        data[game_name] = []

    for game in range(len(urls)):
        if game % 10 == 0:
            print(f'Загружено: {game * 2}%')
        game_name = urls[game][1]
        print(game_name)

        request = requests.get(urls[game][0])
        request_str = request.text.split('"')

        list_of_videos = list(str(request_str).split('videoCardRenderer')[1:])

        mic_data = []
        c = 0
        for i in list_of_videos:
            c += 1
            if c == 6:
                break
            try:
                # pass
                need_lst = i.split("'")

                channel_name = need_lst[128]
                title_tmp = need_lst[96]
                url_video = 'https://www.youtube.com' + need_lst[236]
                title = ''
                need_lst = title_tmp.split(' ')
                for j in range(len(need_lst)):
                    if need_lst[j] != '':
                        if need_lst[j][0] != '\\':
                            title += need_lst[j] + ' '
                mic_data.append([title, channel_name, url_video])
            except:
                print('Ошибка в update_data')
                # need_lst = i.split("'")
                #
                # channel_name = need_lst[128]
                # title_tmp = need_lst[96]
                # print(title_tmp.split(' '))
                #
                # url_video = 'https://www.youtube.com' + need_lst[236]
                # print(channel_name, title_tmp, url_video)

        for z in range(len(mic_data)):
            ch_name = mic_data[z][1]
            title = mic_data[z][0]
            url = mic_data[z][2]
            data[game_name].append({'channel name': ch_name, 'video title': title, 'url': url})
        now = datetime.datetime.now()
        data['last_update_time'] = str(now)
        with open('data/youtube.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    print(f'Загружено: 100%')


# def streams(name):
#     data_youtube = data_get()
#     print("Трансляции YouTube:")
#     print()
#     for i in range(len(data_youtube[name])):
#         print(f'Трансляция №{i + 1}')
#         print(f'   Название трансляции: {data_youtube[name][i]["video title"]}')
#         print(f'   Автор: {data_youtube[name][i]["channel name"]}')
#         print(f'   Ссылка на  трансляцию: {data_youtube[name][i]["url"]}')
#         print()
#     # test1.working_with_streams()


if __name__ == '__main__':
    update_data()
