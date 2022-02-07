from bs4 import BeautifulSoup


def get_data(url):
    driver = webdriver.Edge('msedgedriver.exe')
    driver.get(url)
    with open('../data/project.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)

def parse_games():
    with open('../data/project.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        items = soup.find_all('img')
        games = []
        for game in items:
            half_href = re.sub(r'[^a-zA-Z0-9]', '', game.get('alt'))
            href = 'https://www.facebook.com/gaming/' + half_href.lower()
            games.append(href)
        return games

def parse_stream(games_list:list):
    page = webdriver.Edge('msedgedriver.exe')
    lst = [[]]
    for game_href in games_list:
        page.get(game_href)
        soup = BeautifulSoup(page.page_source, 'lxml')
        main_div = soup.find('div', class_ = 'ms69ghzk d2edcug0')
        hrefs = main_div.find_all('a', class_ ='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p')
        # name = str(hrefs[1].get('aria-label'))
        # author = str(hrefs[2].get('aria-label'))
        # author = author[:author.find('/')]
        # diction = {'name_stream' : name,
        #            'author' : author}
        # print(diction)
        for i in range(5):
            href = hrefs[i].get('href')
            start = str(hrefs[i]).find('>')
            hrefs[i] = str(hrefs[i])[start+1:]
            end = str(hrefs[i]).find('<')
            name = str(hrefs[i])[:end]



            authors = main_div.find_all('span', class_ ='nc684nl6')
            author = str(authors[i])[str(authors[i]).find('<span>')+6:str(authors[i]).find('</span>')]


            lst.append([name,author,href])
        print(game_href)
        print('-' * 20)
        lst[0].append(game_href)
    return lst


def to_json(lst: list):
    t = {}
    j = 1
    for game in range(len(lst[0])):
        game_name = lst[0][game][32:]
        t[game_name] = {}
        for i in range(1 + game * 5, 6 + game * 5):

            text = 'video_' + str(j)
            t[game_name][text] = {}
            stat = {'chanel name' : lst[i][1],
                    'video title' : lst[i][0],
                    'url' : lst[i][2]}
            t[game_name][text] = stat
            j += 1
        j = 1
    return t