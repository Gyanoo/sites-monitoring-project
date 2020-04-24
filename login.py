from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re

class AllegroLogin:
    def __init__(self, mail, password):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        url_login = 'https://allegro.pl/login/form?authorization_uri=https:%2F%2Fallegro.pl%2Fauth%2Foauth%2Fauthorize%3Fclient_id%3Dtb5SFf3cRxEyspDN%26redirect_uri%3Dhttps:%2F%2Fallegro.pl%2Flogin%2Fauth%26response_type%3Dcode%26state%3DhgnqyY&oauth=true'
        url_to_check = 'https://allegro.pl/oferta/uppercut-deluxe-matte-clay-matowa-glinka-probka-3g-8761913887?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi_c=NjVmYjI3ZmMtYjk3Zi00ZWM5LTkwNDItMzgxOTljYmVkN2U4AA&bi_t=ape&referrer=proxy&emission_unit_id=d7895d7b-eba6-4200-9ddf-35bc512a4015'
        self.driver.get(url_login)
        self.driver.set_window_size(1100, 750)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div/button/img').click()
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[2]/button[2]').click()
        self.driver.find_element_by_xpath("//*[contains(text(), 'przejdź dalej')]").click()
        self.driver.find_element_by_id( 'username').send_keys(mail)
        self.driver.find_element_by_id( 'password').send_keys(password)
        self.driver.find_element_by_id( 'login-button').click()
        # xpath_search_input = '/html/body/div[2]/div[1]/nav/div[1]/div[1]/div/div/form/input'
        xpath_search_input = '/html/body/div[2]/div[1]/header/div[1]/div/div/div/form/input'
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(('xpath', xpath_search_input)))
        self.driver.get(url_to_check)
        self.driver.find_element_by_id('add-to-cart-button').click()
        sleep(10)
        self.driver.quit()


class CheckChanges:
    def __init__(self, url, element):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(10)
        if element == '':
            element = '/html/body'
        try:
            self.driver.get(url)
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
        except WebDriverException:
            print("cant reach site.Chrome closed");
        finally:
            print('My work is done')
            self.driver.quit()

class CheckIfPriceLower:
    def __init__(self, url, element, maxPrice):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(10)
        try:
            actualPrice = maxPrice+1
            while actualPrice > float(maxPrice):
                self.driver.get(url)
                # self.driver.find_element_by_xpath("//*[contains(text(), 'Przejdź dalej')]").click()
                priceText = re.split(' ', self.driver.find_element_by_xpath(element).text)
                priceInParts = re.split(',', priceText[0])
                actualPrice = float(priceInParts[0]) + float(priceInParts[1]) / 100
                print(priceText, "   ", priceInParts, "   ", actualPrice)
                sleep(1)
            self.driver.get('https://www.google.com/')
            sleep(10)
        except NoSuchElementException:
            print('Cant find element')
        except WebDriverException:
            print("cant reach site/Chrome closed")
        except AttributeError:
            print("Attribute not found")
        finally:
            print('My work is done')
            self.driver.quit()

# AllegroLogin('ooogyano@gmail.com', 'Python123')
# CheckChanges('file:///Users/michal/Desktop/stare%20ale%20nie%20jare/enroll2.html', '/html/body')
# CheckChanges('file:///Users/michal/Desktop/stare%20ale%20nie%20jare/enroll2.html', '')
# CheckIfPriceLower('https://allegro.pl/oferta/rebel-splendor-edycja-polska-8166800174?bi_m=mpage&','/html/body/div[2]/div[4]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[5]/div/div[1]', 100.0)
# CheckIfPriceLower('file:///Users/michal/Desktop/stare%20ale%20nie%20jare/enroll2.html', '/html/body/h1', 100.0)
