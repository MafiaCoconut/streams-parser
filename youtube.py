import requests
import json
import datetime
from bs4 import BeautifulSoup
import help_files.information as information
import test1


def data_get():
    with open(information.youtube, encoding='utf-8') as file:
        data = json.load(file)
    return data


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
    page = requests.get(information.url, headers=information.headers)
    with open('data/project.html', 'w', encoding='utf-8') as file:
        file.write(page.text)


def update_data():
    # Работа со сохранённой страницей
    get_data()
    with open('data/project.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')

    scripts = soup.find('body').find_all('script')
    items = scripts[13]
    x = str(items)
    lst = x.split('"')
    # print('1!!!!')
    urls = []
    name = ''
    data = {}
    games_name = games_name_get()
    # print(names_of_games)
    for i in range(len(lst)):
        if lst[i] == 'title':
            name = lst[i + 4]
        if lst[i] == 'url':
            url_game = lst[i + 2]
            if 'channel' in url_game:
                urls.append(['https://www.youtube.com' + url_game + '/live', name])
                if name not in games_name:
                    games_name_set(name)
                data[name] = []
                name = ''

    for game in range(50):
        name = urls[game][1]
        if game % 10 == 0:
            print(f'Загружено: {game * 2}%')
            # app.update_percent(str({game * 2}))

        req1 = requests.get(urls[game][0])
        lst1 = req1.text.split('"')

        q = 0
        flag = False
        mic_data = []
        title = ''
        author = []
        url = 'https://www.youtube.com'
        for i in range(len(lst1)):
            if lst1[i] == 'gridVideoRenderer':
                if q == 5:
                    break
                flag = True
            if flag:
                if lst1[i] == 'accessibilityData':
                    x = lst1[i + 4].split(' ')
                    flag1 = False
                    for j in range(len(x)):
                        if flag1:
                            if 'просмотр' in x[j]:
                                author.pop(-1)
                                author.pop(-1)
                                break
                            author.append(x[j + 1])
                        else:
                            if x[j] == 'Автор:':
                                flag1 = True
                                author.append(x[j + 1])
                            else:
                                title += x[j] + ' '
                if lst1[i] == 'webCommandMetadata':
                    x = lst1[i + 4].split(' ')
                    url += x[0]
                    mic_data.append([title, author, url])
                    title = ''
                    author = []
                    url = 'https://www.youtube.com'
                    flag = False
                    q += 1

        for z in range(len(mic_data)):
            ch_name = ''
            for j in mic_data[z][1]:
                ch_name += j + ' '
            title = mic_data[z][0]
            url = mic_data[z][2]
            data[name].append({'channel name': ch_name, 'video title': title, 'url': url})
        now = datetime.datetime.now()
        data['last_update_time'] = str(now)
        with open('data/youtube.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        # print('1111')

def streams(name):
    data_youtube = data_get()
    print("Трансляции YouTube:")
    print()
    for i in range(len(data_youtube[name])):
        print(f'Трансляция №{i + 1}')
        print(f'   Название трансляции: {data_youtube[name][i]["video title"]}')
        print(f'   Автор: {data_youtube[name][i]["channel name"]}')
        print(f'   Ссылка на  трансляцию: {data_youtube[name][i]["url"]}')
        print()
    test1.working_with_streams()


# Обновление информации изменения последнего обновления БД
def update_last_time():
    now = datetime.datetime.now()
    # with open('../help_files/information.py', 'a') as file:
    print(information.database_time['youtube'])
    information.database_time['youtube'] = str(now)
    print(information.database_time['youtube'])


if __name__ == '__main__':
    pass
    update_data()
    # print(games_name_get())
    # check_name_is_in_games_name('Among Us')
    # games_name_set('dgs')