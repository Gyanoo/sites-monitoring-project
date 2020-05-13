from time import sleep
from selenium import webdriver
from functools import partial
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import read_write_data as data
import email_send
from multiprocessing.pool import ThreadPool
import login
import re
import threading


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


def check_if_price_lower(element, sd):
    # login.allegro_login(element['login'], element['password'])
    print(threading.get_ident())
    allegro_login = element["login"]
    allegro_password = element["password"]
    # options = webdriver.ChromeOptions()
    # options.add_argument("disable-gpu")
    # options.add_argument("headless")
    # options.add_argument("no-default-browser-check")
    # options.add_argument("no-first-run")
    # options.add_argument("no-sandbox")
    # with this options driver will work in background
    driver = webdriver.Chrome()#options=options)
    driver.implicitly_wait(10)
    url_login = 'https://allegro.pl/login/form?authorization_uri=https:%2F%2Fallegro.pl%2Fauth%2Foauth%2Fauthorize%3Fclient_id%3Dtb5SFf3cRxEyspDN%26redirect_uri%3Dhttps:%2F%2Fallegro.pl%2Flogin%2Fauth%26response_type%3Dcode%26state%3DhgnqyY&oauth=true'
    driver.get(url_login)
    driver.set_window_size(1100, 750)
    driver.find_element_by_xpath("//*[contains(text(), 'przejdź dalej')]").click()
    driver.find_element_by_id('username').send_keys(allegro_login)
    driver.find_element_by_id('password').send_keys(allegro_password)
    driver.find_element_by_id('login-button').click()
    print("zalogowałem się")
    actualPrice = float(element['price'])
    driver.get(element["link"])
    try:
        while actualPrice >= float(element['price']):
            driver.get(element["link"])
            priceText = re.split(' ', driver.find_element_by_xpath(element['xpath']).text)
            priceInParts = re.split(',', priceText[0])
            actualPrice = float(priceInParts[0]) + float(priceInParts[1]) / 100
            print(priceText, "   ", priceInParts, "   ", actualPrice)
            sleep(element["time"])
            # if sd['isTerminatedP2']:
            #     print("breaking")
            #     break
    except NoSuchElementException:
        print('Cant find element')
    except WebDriverException:
        print("cant reach site/Chrome closed")
    except AttributeError:
        print("Attribute not found")
    finally:
        print('My work is done')
        driver.quit()
        if actualPrice < element["price"]:
            email_send.send_email(element["email_to_send"], element["link"], actualPrice)


def start_monitor(shared_dict):
    print("I'm starting to monitor")
    actual_index = 0
    pools = {}
    while True:
        if shared_dict['isTerminatedP2']:
            shared_dict['isTerminatedP2'] = False
        elements_all = data.read_monitored_elements()
        for e in elements_all:
            if e["is_done"] is False and e["is_on"] is True and e not in pools.values():
                print("dodaje")
                globals()['pool%s' % actual_index] = ThreadPool(processes=1)
                pools[globals()['pool%s' % actual_index]] = e
                monitor_fun = partial(check_if_price_lower, sd=shared_dict)
                # globals()['pool%s' % actual_index].map_async(monitor_fun, e)
                globals()['pool%s' % actual_index].apply_async(monitor_fun, (e,))
                # globals()['pool%s' % actual_index].close()
                actual_index += 1
                sleep(0.5)
            elif (e["is_done"] is True or e["is_on"] is False) and e in pools.values:
                print("usuwam")
                pool_to_remove = list(pools.keys())[list(pools.values()).index(e)]
                pools.pop(pool_to_remove)
                pool_to_remove.close()
                pool_to_remove.join()

        # if len(elements_to_monitor) != 0:
        #     elements_sorted = sorted(elements_to_monitor, key=lambda i: i['time'])
        #     print(shared_dict['isTerminatedP2'])
        #     pool = ThreadPool(processes=len(elements_sorted))
        #     monitor_fun = partial(check_if_price_lower, sd=shared_dict)
        #     pool.map_async(monitor_fun, elements_sorted)
        #     pool.close()
        #     pool.join()

# def start_monitor(shared_dict):
#     while True:
#         if shared_dict['isTerminatedP2']:
#             shared_dict['isTerminatedP2'] = False
#         print("start")
#         elements_all = data.read_monitored_elements()
#         elements_to_monitor = []
#         for e in elements_all:
#             if e["is_done"] is False and e["is_on"] is True:
#                 elements_to_monitor.append(e)
#         if len(elements_to_monitor) != 0:
#             elements_sorted = sorted(elements_to_monitor, key=lambda i: i['time'])
#             print(shared_dict['isTerminatedP2'])
#             pool = ThreadPool(processes=len(elements_sorted))
#             monitor_fun = partial(check_if_price_lower, sd=shared_dict)
#             pool.map_async(monitor_fun, elements_sorted)
#             pool.close()
#             pool.join()

if __name__ == "__main__":
    d = {'isTerminatedP2': False}
    start_monitor(d)


# def monitor_element(element, sd):
#     new_price = element["price"]
#     while True:
#         proc_name = multiprocessing.current_process().name
#         print(proc_name)
#         new_price = check_if_price_lower(element["link"], element["xpath"], element["price"], element["time"])
#         sleep(element["time"])
#         # if new_price != float(element["price"]):
#         #     email_send.send_email(element["email_to_send"], element["link"], new_price)
#         #     break
#         if sd:
#             break

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


#backup
# def check_if_price_lower(element, sd):
#     # login.allegro_login(element['login'], element['password'])
#     allegro_login = element["login"]
#     allegro_password = element["password"]
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(30)
#     url_login = 'https://allegro.pl/login/form?authorization_uri=https:%2F%2Fallegro.pl%2Fauth%2Foauth%2Fauthorize%3Fclient_id%3Dtb5SFf3cRxEyspDN%26redirect_uri%3Dhttps:%2F%2Fallegro.pl%2Flogin%2Fauth%26response_type%3Dcode%26state%3DhgnqyY&oauth=true'
#     driver.get(url_login)
#     driver.set_window_size(1100, 750)
#     driver.find_element_by_xpath("//*[contains(text(), 'przejdź dalej')]").click()
#     driver.find_element_by_id('username').send_keys(allegro_login)
#     driver.find_element_by_id('password').send_keys(allegro_password)
#     driver.find_element_by_id('login-button').click()
#     options = webdriver.ChromeOptions()
#     options.add_argument("disable-gpu")
#     options.add_argument("headless")
#     options.add_argument("no-default-browser-check")
#     options.add_argument("no-first-run")
#     options.add_argument("no-sandbox")
#     # with this options driver will work in background
#     driver = webdriver.Chrome(options=options)
#     driver.implicitly_wait(10)
#     actualPrice = element['price']
#     try:
#         while actualPrice >= float(element['price']):
#             driver.get(element["link"])
#             priceText = re.split(' ', driver.find_element_by_xpath(element['xpath']).text)
#             priceInParts = re.split(',', priceText[0])
#             actualPrice = float(priceInParts[0]) + float(priceInParts[1]) / 100
#             print(priceText, "   ", priceInParts, "   ", actualPrice)
#             sleep(element["time"])
#             if sd:
#                 break
#     except NoSuchElementException:
#         print('Cant find element')
#     except WebDriverException:
#         print("cant reach site/Chrome closed")
#     except AttributeError:
#         print("Attribute not found")
#     finally:
#         print('My work is done')
#         driver.quit()
#         if actualPrice < element["price"]:
#             email_send.send_email(element["email_to_send"], element["link"], actualPrice)
