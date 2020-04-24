import json


def read_json_file():
    with open("data.json") as file:
        data = json.load(file)
    return data


def read_monitored_elements():
    with open("data.json") as file:
        data = json.load(file)
    elements_list = data["monitored_elements"]
    return elements_list


def add_monitored_elements(name, link, is_done):
    data = read_json_file()

    for e in data["monitored_elements"]:
        if e['link'] == link and e['is_done'] is False:
            print("This page is already monitored")
            return
        elif e['link'] == link and e['is_done'] is True:
            e["is_done"] = False

    element = {'name': name, 'link': link, 'is_done': is_done}
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


if __name__ == "__main__":
    print(read_monitored_elements())
    add_monitored_elements("Apple iPhone 11",
                           "https://allegro.pl/oferta/apple-iphone-11-64gb-a13-dual-sim-zielony-8752755558?bi_s=ads"
                           "&bi_m=listing%3Adesktop%3Acategory&bi_c"
                           "=MDAzZjE0MmYtNTFmMy00YWZlLTgwNzktOWY2ZTg3OGRkMzBhAA&bi_t=ape&referrer=proxy"
                           "&emission_unit_id=b0da8330-667f-4c27-a495-084a70aea6af",
                           False)
