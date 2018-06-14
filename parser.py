from selenium import webdriver

chromedriver = '/home/max/Programs/chromedriver'
URL = 'https://1xstavka.ru/live/Football/'

class Parser:
    def __init__(self):
        pass

    def start(self):
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get(URL)
        page = self.driver.find_element_by_id('games_content')
        list_of_games = page.find_elements_by_class_name('c-events__item_game')
        print(len(list_of_games))
        for game in list_of_games:
            link_to_game = game.find_element_by_class_name('c-events-scoreboard').find_element_by_tag_name('a').get_attribute('href')
            id_game = link_to_game.split('/')[-2].split('-')[0]
            print(link_to_game)
            print(id_game)

parser= Parser()
parser.start()