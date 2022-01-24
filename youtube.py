import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3

from bs4 import BeautifulSoup
import information
import main


def data_get():
    with open(information.youtube, encoding='utf-8') as file:
        data = json.load(file)
    return data


def games_name_set(name):
    with open('data/games_name', 'a', encoding='utf-8') as file:
        word = name+';'
        file.write(word)


def get_data():
    page = requests.get(information.url, headers=information.headers)
    with open('data/project.html', 'w', encoding='utf-8') as file:
        file.write(page.text)


def update_data():
    # Работа со сохранённой страницей
    get_data()
    with open('data/project.html', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
    # print(page)

    # Работа на прямую с сайтом
    # page = requests.get(url, headers=headers)
    # soup = BeautifulSoup(page.text, 'lxml')

    scripts = soup.find('body').find_all('script')
    items = scripts[13]
    x = items.text
    lst = x.split('"')

    urls = []
    name = ''
    data = {}
    games_name = main.games_name_get()
    # print(games_name)
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
            print(f'Загружено: {game*2}%')

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
        with open(information.youtube, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
