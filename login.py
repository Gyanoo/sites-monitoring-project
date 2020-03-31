from time import sleep
from selenium import webdriver

class AllegroLogin:
    def __init__(self, mail, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://allegro.pl")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[8]/div/div[2]/div/div[2]/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/header/div/nav/div[4]/button/img[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/header/div/nav/div[4]/div/div/div[2]/div/div[3]/a[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/ui-view/div/div/div/main/div/section[1]/div/section[1]/form/div[1]/div[1]/div/div/input').send_keys(mail)
        self.driver.find_element_by_xpath('/html/body/div[2]/ui-view/div/div/div/main/div/section[1]/div/section[1]/form/div[1]/div[2]/div/div/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[2]/ui-view/div/div/div/main/div/section[1]/div/section[1]/form/article/div/div/section[2]/button/span').click()
        sleep(1)
        self.driver.get("https://allegro.pl/oferta/uppercut-deluxe-matte-clay-matowa-glinka-probka-3g-8761913887?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi_c=NjVmYjI3ZmMtYjk3Zi00ZWM5LTkwNDItMzgxOTljYmVkN2U4AA&bi_t=ape&referrer=proxy&emission_unit_id=d7895d7b-eba6-4200-9ddf-35bc512a4015")
        # sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/form/div[2]/button').click()
        sleep(20)

AllegroLogin('ooogyano@gmail.com', 'Python123')
