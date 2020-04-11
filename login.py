from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AllegroLogin:
    def __init__(self, mail, password):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        url_login = 'https://allegro.pl/login/form?authorization_uri=https:%2F%2Fallegro.pl%2Fauth%2Foauth%2Fauthorize%3Fclient_id%3Dtb5SFf3cRxEyspDN%26redirect_uri%3Dhttps:%2F%2Fallegro.pl%2Flogin%2Fauth%26response_type%3Dcode%26state%3DhgnqyY&oauth=true'
        url_to_check = 'https://allegro.pl/oferta/uppercut-deluxe-matte-clay-matowa-glinka-probka-3g-8761913887?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi_c=NjVmYjI3ZmMtYjk3Zi00ZWM5LTkwNDItMzgxOTljYmVkN2U4AA&bi_t=ape&referrer=proxy&emission_unit_id=d7895d7b-eba6-4200-9ddf-35bc512a4015'
        self.driver.get(url_login)
        self.driver.set_window_size(1100, 750)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div/button/img').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/button[2]').click()
        self.driver.find_element_by_id( 'username').send_keys(mail)
        self.driver.find_element_by_id( 'password').send_keys(password)
        self.driver.find_element_by_id( 'login-button').click()
        xpath_search_input = '/html/body/div[2]/div[1]/nav/div[1]/div[1]/div/div/form/input'

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(('xpath', xpath_search_input)))
        self.driver.get(url_to_check)
        self.driver.find_element_by_id('add-to-cart-button').click()
        sleep(10)
        self.driver.quit()

# AllegroLogin('ooogyano@gmail.com', 'Python123')


class CheckChanges:
    def __init__(self, url, element):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(10)

        try:
            self.driver.get(url)
            # mainPage = self.driver.find_element_by_tag_name('body').text
            mainPage = self.driver.find_element_by_xpath(element).text
            actualPage = mainPage
            while mainPage == actualPage:
                self.driver.get(url)
                actualPage = self.driver.find_element_by_xpath(element).text
                sleep(1)
            self.driver.get('https://www.google.com/')
            sleep(10)
        except NoSuchElementException:
            print('Cant find element')
        finally:
            print('My work is done')


CheckChanges('file:///Users/michal/Desktop/stare%20ale%20nie%20jare/enroll2.html', '/html/body/table/tbody/tr[6]/td/div')
