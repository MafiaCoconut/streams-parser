# # lst = ['Apex Legends', 'Garena Free Fire', 'Battlegrounds Mobile India', 'Minecraft', 'Grand Theft Auto V', 'Mario Kart 8 Deluxe', 'Fate/Grand Order', 'Fortnite', 'League of Legends', 'Super Smash Bros. Ultimate', 'Lineage W', 'Roblox', 'PUBG MOBILE', 'Gates of Olympus Slot Pragmatic', 'Dota 2', 'World of Tanks', 'Knives Out', 'Counter-Strike: Global Offensive', 'BeamNG.drive', 'Valorant', 'Animal Crossing: New Horizons', 'Friday Night Funkin’', 'PlayerUnknown’s Battlegrounds', 'Pokémon Unite', 'ARK: Survival Evolved', 'Genshin Impact', 'Shadowverse', 'Dead by Daylight', 'Pokémon Brilliant Diamond and Shining Pearl', 'Puyo Puyo Champions', 'Arena of Valor', 'Garena Free Fire MAX', 'PUBG MOBILE LITE', 'Uma Musume: Pretty Derby', 'FIFA 22', 'Lineage2M', 'Resident Evil 5', 'Candy Crush Saga', 'Ragnarök Online', 'Lost Ark', 'Poppy Playtime', 'Red Ball 4', 'Ball Run 2048', 'Grand Theft Auto: San Andreas', 'Slot Pragmatic Play Aztec Gems', 'Brawl Stars', 'StarCraft: Remastered', 'Dragon Quest XI', 'Plants vs. Zombies', 'Diablo II: Resurrected']
# # print(*lst, sep=';')
# # import keyword
# # keyword.iskeyword(s)
# # print('1!!!')
# import datetime
# now = datetime.datetime.now()
# print(str(now))
# print(now.isoformat().replace('T', ' '))
# # information.database_time['youtube'] = [now.hour, now.minute, now.second, now]

import requests
import json
import datetime
from bs4 import BeautifulSoup
import information



# Работа со сохранённой страницей
with open('data/project.html', encoding='utf-8') as file:
    soup = BeautifulSoup(file.read(), 'lxml')

scripts = soup.find('body').find_all('script')
# print(scripts)
items = scripts[13]
print(items)
x = str(items)
print(x)
y = x.split('"')
print(y)

# print(type(items))
# x = items.text
# print(type(x), x)
# lst = x.split('""')
# print(lst)