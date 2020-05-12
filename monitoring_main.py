#TODO stworzenie funkcji obslugujacej żądane polecenia monitorowania. Głównie Odpalanie monitorowania (z pliku monitoring.py i
#killowanie monitorowania. Najlepiej by było zczytywac dane strony do monitorowania wraz z mailem itd. z JSONa, a podawac jej np. tylko link
#i wartosc co chcemy zrobic. np:
#monitoring_main(link, "kill") by wyszukiwał proces który trzeba zabic i go zabijał.
#czyli bedzie trzeba trzymac jakas strukturke z parami link-idprocesu/jakis odnosnik do niego, zalezy jak dziala ten multiprocessing
import multiprocessing
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re
import os
import read_write_data as data
import email_send
from multiprocessing.pool import ThreadPool
#
# pool = ThreadPool()
_FINISH = False


def check_changes(url, element):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    if element == '':
        element = '/html/body'
    try:
        driver.get(url)
        mainPage = driver.find_element_by_xpath(element).text
        actualPage = mainPage
        while mainPage == actualPage:
            driver.get(url)
            actualPage = driver.find_element_by_xpath(element).text
            sleep(1)
        driver.get('https://www.google.com/')
        sleep(10)
    except NoSuchElementException:
        print('Cant find element')
    except WebDriverException:
        print("cant reach site.Chrome closed")
    finally:
        print('My work is done')
        driver.quit()


def check_if_price_lower(url, element, max_price, sleep_time):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        actualPrice = max_price+1
        while actualPrice > float(max_price):
            driver.get(url)
            # self.driver.find_element_by_xpath("//*[contains(text(), 'Przejdź dalej')]").click()
            priceText = re.split(' ', driver.find_element_by_xpath(element).text)
            priceInParts = re.split(',', priceText[0])
            actualPrice = float(priceInParts[0]) + float(priceInParts[1]) / 100
            print(priceText, "   ", priceInParts, "   ", actualPrice)
            sleep(sleep_time)
        # driver.get('https://www.google.com/')
        # sleep(10)
    except NoSuchElementException:
        print('Cant find element')
    except WebDriverException:
        print("cant reach site/Chrome closed")
    except AttributeError:
        print("Attribute not found")
    finally:
        print('My work is done')
        driver.quit()
        return actualPrice


def monitor_element(element):
    new_price = element["price"]
    while True:
        proc_name = multiprocessing.current_process().name
        print(proc_name)
        new_price = check_if_price_lower(element["link"], element["xpath"], element["price"], element["time"])
        sleep(element["time"])
        # if new_price != float(element["price"]):
        #     email_send.send_email(element["email_to_send"], element["link"], new_price)
        #     break
        if _FINISH:
            break


def start_monitor():
    print("start")
    elements_all = data.read_monitored_elements()
    elements_to_monitor = []
    for e in elements_all:
        if e["is_done"] is False and e["is_on"] is True:
            elements_to_monitor.append(e)
    elements_sorted = sorted(elements_to_monitor, key=lambda i: i['time'])
    global _FINISH
    pool = ThreadPool(processes=len(elements_sorted))
    pool.map(monitor_element, elements_sorted)

    # sleep(3)
    # _FINISH = True
    # pool.terminate()
    # pool.join()

def stop_run_monitor():
    pass
#     print("stop")
#     _FINISH = True
#     pool.terminate()
#     pool.join()


if __name__ == "__main__":
    start_monitor()









#
# class Monitor:
#     def __init__(self):
#         # self.pool = ThreadPool()
#         self.start_monitor()
#
#     def check_if_price_lower(self, url, element, max_price, sleep_time):
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(10)
#         try:
#             actualPrice = max_price + 1
#             while actualPrice > float(max_price):
#                 driver.get(url)
#                 # self.driver.find_element_by_xpath("//*[contains(text(), 'Przejdź dalej')]").click()
#                 priceText = re.split(' ', driver.find_element_by_xpath(element).text)
#                 priceInParts = re.split(',', priceText[0])
#                 actualPrice = float(priceInParts[0]) + float(priceInParts[1]) / 100
#                 print(priceText, "   ", priceInParts, "   ", actualPrice)
#                 sleep(sleep_time)
#             # driver.get('https://www.google.com/')
#             # sleep(10)
#         except NoSuchElementException:
#             print('Cant find element')
#         except WebDriverException:
#             print("cant reach site/Chrome closed")
#         except AttributeError:
#             print("Attribute not found")
#         finally:
#             print('My work is done')
#             driver.quit()
#             return actualPrice
#
#     def monitor_element(self, element):
#         new_price = element["price"]
#         while True:
#             # print( element["time"])
#             proc_name = multiprocessing.current_process().name
#             print(proc_name)
#             new_price = self.check_if_price_lower(element["link"], element["xpath"], element["price"], element["time"])
#             # sleep(element["time"])
#             sleep(1)
#             # if new_price != float(element["price"]):
#             #     email_send.send_email(element["email_to_send"], element["link"], new_price)
#             #     break
#             if _FINISH:
#                 break
#
#     def start_monitor(self):
#         print(os.cpu_count())
#         elements_all = data.read_monitored_elements()
#         elements_to_monitor = []
#         for e in elements_all:
#             if e["is_done"] is False and e["is_on"] is True:
#                 elements_to_monitor.append(e)
#         elements_sorted = sorted(elements_to_monitor, key=lambda i: i['time'])
#         global _FINISH
#         print(elements_sorted)
#         self.pool = ThreadPool()
#         self.pool.map(self.monitor_element, elements_sorted)
#         self.pool.terminate()
#         print("end")
#         # sleep(3)
#         # _FINISH = True
#         # pool.terminate()
#         # pool.join()
#
#     def stop_run_monitor(self):
#         print("stop")
#         # _FINISH = True
#         # self.pool.terminate()
#         # self.pool.join()
#