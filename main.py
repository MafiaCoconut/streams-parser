import requests
from requests.auth import HTTPBasicAuth
import json
import sqlite3
import os
import re
import time
from bs4 import BeautifulSoup
# from selenium import webdriver


def get_data(url, headers):
    page = requests.get(url, headers=headers)
    with open('data/project.html', 'w', encoding='utf-8') as file:
        file.write(page.text)


def work_with_main_page(url, headers, games_name):
    # Работа со сохранённой страницей
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
    # games_name = []
    for i in range(len(lst)):
        if lst[i] == 'title':
            name = lst[i + 4]

        if lst[i] == 'url':
            url_game = lst[i + 2]
            if 'channel' in url_game:
                urls.append(['https://www.youtube.com' + url_game + '/live', name])
                # lst_games.append(name)
                # if name not in games_name:
                #     games_name
                data[name] = []
                name = ''

    # for game in range(50):
    for game in range(50):
        name = urls[game][1]
        print(name)

        req1 = requests.get(urls[game][0])
        lst1 = req1.text.split('"')

        # with open('data/Minecraft.html', 'w', encoding='utf-8') as file:
        #     file.write(req1.text)

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
            print(mic_data[z])
            ch_name = ''
            for j in mic_data[z][1]:
                ch_name += j + ' '
            title = mic_data[z][0]
            url = mic_data[z][2]
            data[name].append({'channel name': ch_name, 'video title': title, 'url': url})
        with open('data/data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    return games_name


def public(uuid=0):
    lst = ['Apex Legends', 'Garena Free Fire', 'Battlegrounds Mobile India', 'Minecraft', 'Grand Theft Auto V', 'Mario Kart 8 Deluxe', 'Fate/Grand Order', 'Fortnite', 'League of Legends', 'Super Smash Bros. Ultimate', 'Lineage W', 'Roblox', 'PUBG MOBILE', 'Gates of Olympus Slot Pragmatic', 'Dota 2', 'World of Tanks', 'Knives Out', 'Counter-Strike: Global Offensive', 'BeamNG.drive', 'Valorant', 'Animal Crossing: New Horizons', 'Friday Night Funkin’', 'PlayerUnknown’s Battlegrounds', 'Pokémon Unite', 'ARK: Survival Evolved', 'Genshin Impact', 'Shadowverse', 'Dead by Daylight', 'Pokémon Brilliant Diamond and Shining Pearl', 'Puyo Puyo Champions', 'Arena of Valor', 'Garena Free Fire MAX', 'PUBG MOBILE LITE', 'Uma Musume: Pretty Derby', 'FIFA 22', 'Lineage2M', 'Resident Evil 5', 'Candy Crush Saga', 'Ragnarök Online', 'Lost Ark', 'Poppy Playtime', 'Red Ball 4', 'Ball Run 2048', 'Grand Theft Auto: San Andreas', 'Slot Pragmatic Play Aztec Gems', 'Brawl Stars', 'StarCraft: Remastered', 'Dragon Quest XI', 'Plants vs. Zombies', 'Diablo II: Resurrected']

    u = 'MafiaCoconut'
    p = 'QaQaQaQa0'

    with open('data/test1.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(data)
    print(data['Grand Theft Auto V'])

    endpoint = 'http://localhost/drupal/jsonapi/node/article'+('' if uuid==0 else ("/"+uuid))

    headers = {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json'
    }
    for i in lst:
        for j in range(5):
            print(i)
            try:
                print(data[i][j])
                # print(data[i][j], end='\n')

                payload = {
                    "data": {
                        "type": "node--article",
                        "attributes": {
                            "title": i,
                            "body": {
                                "value": f" Платформа: Youtube\n Название канала: {data[i][j]['channel name']}\n Название видео: {data[i][j]['video title']}\n Ссылка: {data[i][j]['url']}\n Теги: #{i}",
                                "format": "plain_text",
                            }
                        }
                    }
                }
                requests.post(endpoint, headers=headers, auth=(u, p), json=payload)
            except Exception:
                pass


def main():
    url = 'https://www.youtube.com/gaming/games'
    headers = {
        'accept': 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61 (Edition Yx GX 03)'
    }
    # get_data(url, headers)

    games_name = []
    with open('data/games_name', 'r', encoding='utf-8') as file:
        games_name = list(file.read().split(';'))

    # games_name = work_with_main_page(url, headers)
    # lst = work_with_main_page1(url, headers)
    # public()


if __name__ == '__main__':
    main()
