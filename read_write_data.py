import json
from selenium import webdriver


def read_json_file():
    with open("data.json") as file:
        data = json.load(file)
    return data


def read_monitored_elements():
    with open("data.json") as file:
        data = json.load(file)
    elements_list = data["monitored_elements"]
    return elements_list


def add_monitored_elements(login, email_to_send, password, link):
    data = read_json_file()
    for e in data["monitored_elements"]:
        if e['link'] == link and e['is_done'] is False:
            print("This page is already monitored")
            raise KeyError
        elif e['link'] == link and e['is_done'] is True:
            e["is_done"] = False
    name = get_name(link)
    element = {
                'name': name,
                'link': link,
                'is_done': False,
                'login': login,
                'password': password,
                'email_to_send': email_to_send
               }
    data["monitored_elements"].append(element)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)


def delete_monitored_element(link):
    data = read_json_file()
    for e in data["monitored_elements"]:
        if e['link'] == link:
            data["monitored_elements"].remove(e)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)


def get_element(link):
    elements = read_monitored_elements()
    for element in elements:
        if element['link'] == link:
            return element
    return None


def get_name(link):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-gpu")
    options.add_argument("headless")
    options.add_argument("no-default-browser-check")
    options.add_argument("no-first-run")
    options.add_argument("no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.set_window_rect(-1000, -1000, 1100, 750)
    driver.implicitly_wait(30)
    driver.get(link)
    driver.find_element_by_xpath("//*[contains(text(), 'przejdź dalej')]").click()
    text = driver.find_elements_by_tag_name('h1')[0].get_attribute("textContent")
    name = ''
    if len(text) >= 34:
        i = 0
        for letter in text:
            name += letter
            i += 1
            if i == 34:
                break
        name += "..."
    else:
        name += text

    driver.quit()
    return name


if __name__ == "__main__":
    # print(read_monitored_elements())
    add_monitored_elements("https://allegro.pl/oferta/iphone-11-64gb-red-czerwony-nowy-gw-apple-od-reki-8817870462?reco_id=1d92b713-86dd-11ea-a373-ecf4bbd61370&sid=f8bddad5d737919e6c726c989b66bdbe96499e13bc806f55bd0c404f69ac7020",
                           False)
    # print(get_element("sfdad"))
    # get_name("https://allegro.pl/oferta/sluchawki-hyperx-cloud-alpha-hx-hsca-gd-nap-gaming-9140143545?reco_id=2645c81a-8634-11ea-9b23-b02628c7f910&sid=3ec404f37aa2fad6253fa5dd6bb023427743f77ee2f01bb84454c4701b8c0118")