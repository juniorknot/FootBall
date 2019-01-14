from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as NoElement
from selenium.common.exceptions import StaleElementReferenceException as NotAttached
from selenium.common.exceptions import ElementNotVisibleException as NotVisible

from selenium.webdriver.common.keys import Keys

# chromedriver = '/home/max/Programs/chromedriver'
URL = 'https://1xstavka.ru/'
# MIRROR = 'http://bet-1xbet.ru/zerkalo-sajta-1xbet/'
matches = []
errors = []
gtime = 17
bet = 20

class Parser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
    def start(self):
        try:

            # self.driver.minimize_window()
            # self.driver.get(MIRROR)
            # self.going_by_mirror()
            self.driver.refresh()
            time.sleep(2)
            try:
                self.login()
            except Exception as e:
                print(e)
            self.tuning()

            page = self.driver.find_element_by_id('live_bets_on_main')

            list_of_games = page.find_elements_by_class_name('c-events__item_game')
            print('Всего игр на странице: ', len(list_of_games))
            self.driver.minimize_window()
            for game in list_of_games:
                balls_ok = False
                link_to_game = game.find_element_by_class_name('c-events-scoreboard').find_element_by_tag_name('a').get_attribute('href')
                try:
                    game_time = int(game.find_element_by_class_name('c-events__time').text.split(':')[0])
                except ValueError:
                    game_time = gtime + 5
                except NoElement:
                    game_time = gtime + 5
                game_ID = link_to_game.split('/')[-2].split('-')[0]
                print(game_ID)
                balls_list = game.find_elements_by_class_name('c-events-scoreboard__cell--all')
                if len(balls_list)>1:
                    # if int(balls_list[0].text)>1 or int(balls_list[1].text)>1:
                    if (int(balls_list[0].text) + int(balls_list[1].text)) > 1:
                        balls_ok = True

                if balls_ok and game_time <gtime and game_ID not in matches:
                # if 45>game_time>0:
                    game_page = GamePage(link_to_game)

                    print('Now we\'ll make the bet')
                    try:
                        game_page.login()
                    except Exception:
                        pass

                    try:
                        game_page.make_bet()
                        matches.append(game_ID)
                    except Exception as e:
                        errors.append(e)
                        print(errors)
                    game_page.driver.quit()

                if game_time >=gtime:
                    if game_ID in matches:
                        matches.remove(game_ID)

                print('Time: ', game_time, balls_list[0], ':', balls_list[1])
                print(link_to_game)
                print('matches: ', matches)
            # self.driver.quit()
        except NotAttached:
            # self.driver.quit()
            pass

    def going_by_mirror(self):
        link1 = self.driver.find_elements_by_xpath('//a[@class="buttons btn_red center"]')[0]
        link1.click()
        time.sleep(0.2)



    def login(self):
        button = self.driver.find_element_by_xpath('//div[@id="loginout"]').find_element_by_class_name('name')
        if button.text == 'ВОЙТИ':
            button.click()


        time.sleep(0.2)
        login_window = self.driver.find_element_by_xpath(
            '//input[@id="userLogin"]')
        login_window.click()
        time.sleep(0.2)
        login_window.send_keys('10935003')

        pass_window = self.driver.find_element_by_xpath(
            '//input[@id="userPassword"]')
        pass_window.click()
        time.sleep(0.2)
        pass_window.send_keys('QWE123ZAQ!')
        time.sleep(1)
        pass_window.send_keys(Keys.ENTER)
        # login_key = self.driver.find_element_by_xpath(
        #     '//a[@class="enter_button_main"]')
        # login_key.click()
        time.sleep(3)

    def tuning(self):    	
        try:
            self.driver.find_element_by_xpath(
                '//div[@class="box-modal_close arcticmodal-close"]').click()
        except NoElement:
            pass
        except NotVisible:
            pass
        lxbet_button = self.driver.find_element_by_xpath(
            '//div[@id="headerLogo"]')
        lxbet_button.click()
        time.sleep(1)
        amount_button10 = self.driver.find_element_by_xpath(
            '//div[@class="labelFdropAct"]')
        amount_button10.click()
        time.sleep(0.1)
        self.driver.find_element_by_xpath(
            '//div[@data-type="200"]').click()  # changing amount of games to 200
        try:
            football_button = self.driver.find_element_by_xpath(
                '//label[@title="Футбол"]')
            football_button.click()
        except NotVisible:
            self.start()
        # filter_button = self.driver.find_element_by_xpath(
        #     '//input[@class = "multiselect__input"]')
        # filter_button.click()
        # filter_1_period_button = self.driver.find_elements_by_xpath(
        #     '//span[@class="multiselect__option multiselect__option--highlight"]')
        # print('FILTER: ', len(filter_1_period_button))
        time.sleep(2)

class GamePage:
    def __init__(self, link):
        self.link = link
        self.driver = webdriver.Chrome()
        self.driver.get(link)

    def start(self):

        try:
            pass
            # commands = self.driver.find_element_by_class_name('db-stats__top').text.split('\n')
            # self.part = self.driver.find_element_by_xpath('//a[@class="db-sport__linkTime"]').text.replace('-й Тайм', '')
            # print(self.part)
            # table = self.driver.find_element_by_class_name('db-stats__bottom')
            #
            # table_rows = table.find_elements_by_class_name('db-stats-table__group')
            # for row in table_rows:
            #     x = row.text.split('\n')
            #
            #     print(x[1])
            #     print(commands[0]+'     '+commands[1])
            #     print(x[0]+'                        '+x[2])
            # del(commands)
            # del(table)
            # del(table_rows)


        except NoElement:
            pass
        # finally:
        #     self.driver.quit()
    def login(self):
        button = self.driver.find_element_by_xpath('//div[@id="loginout"]').find_element_by_class_name('name')
        if button.text == 'ВОЙТИ':
            button.click()


        time.sleep(0.2)
        login_window = self.driver.find_element_by_xpath(
            '//input[@id="userLogin"]')
        login_window.click()
        time.sleep(0.2)
        login_window.send_keys('10935003')

        pass_window = self.driver.find_element_by_xpath(
            '//input[@id="userPassword"]')
        pass_window.click()
        time.sleep(0.2)
        pass_window.send_keys('QWE123ZAQ!')
        time.sleep(1)
        pass_window.send_keys(Keys.ENTER)
        # login_key = self.driver.find_element_by_xpath(
        #     '//a[@class="enter_button_main"]')
        # login_key.click()
        time.sleep(3)





    def make_bet(self):
        # self.login()
        time.sleep(1)
        box_to_choose = self.driver.find_element_by_class_name('dopEvsWrap')
        box_to_choose.click()
        time.sleep(1)
        time1 = self.driver.find_element_by_xpath('//li[@data-option-array-index="1"]')
        time1.click()
        bets = self.driver.find_elements_by_xpath('//span[@class = "bet_type"]')
        for bet in bets:
            if bet.text == '2.5 Б':
                bet.click()
                time.sleep(0.5)
                input_window = self.driver.find_element_by_xpath('//input[@class = "c-spinner__input bet_sum_input"]')
                input_window.send_keys('20')
                time.sleep(0.5)
                input_window.send_keys(Keys.ENTER)
                time.sleep(15)
                break





    def login(self):
        elements = self.driver.find_elements_by_xpath('//span[@class="name"]')
        for element in elements:
            text = element.text
            if text == 'ВОЙТИ':
                element.click()

        time.sleep(0.2)
        login_window = self.driver.find_element_by_xpath(
            '//input[@id="userLogin"]')
        login_window.click()
        time.sleep(0.2)
        login_window.send_keys('10935003')

        pass_window = self.driver.find_element_by_xpath(
            '//input[@id="userPassword"]')
        pass_window.click()
        time.sleep(0.2)
        pass_window.send_keys('QWE123ZAQ!')
        time.sleep(1)
        login_key = self.driver.find_element_by_xpath(
            '//a[@class="enter_button_main"]')
        login_key.click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath(
                '//div[@class="box-modal_close arcticmodal-close"]').click()
        except NoElement:
            pass






if __name__ == "__main__":
    parser = Parser()
    while True:
        try:
            parser.start()
        except Exception:
            parser.start()