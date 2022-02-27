import json
url = 'https://www.youtube.com/gaming/games'
headers = {
    'accept': 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61 (Edition Yx GX 03)'
}
youtube = '../data/youtube.json'
facebook_gaming = '../data/facebook_gaming.json'
database_time = {
        'youtube': ''
    }

games_name = []



def update_games_name():
    with open('help_files/name_of_games.txt', encoding='utf-8') as file:
        games_name = list(file.read().split(';'))
        return games_name


def update_last_time():
    with open('../data/youtube.json', encoding='utf-8') as file:
        data = json.load(file)
        database_time['youtube'] = data['last_update_time']
        return database_time['youtube']
        # print(database_time['youtube'])

# print(update_last_time())
