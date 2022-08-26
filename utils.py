import os, sys
import random, csv
from PIL import Image
from datetime import datetime
import json
from tqdm import tqdm

uni_cnts = 0


def global_counter():
    global uni_cnts
    uni_cnts += 1


def probability(percentage_chance
                ):  # "percentage_chance" chance to return True, else False
    global uni_cnts
    while uni_cnts <= 1000:
        global_counter()
        cnt = random.randrange(1, 100) / 100
        if cnt < percentage_chance:
            # do something
            return True

        else:
            # do something
            return False
    uni_cnts = 0


def get_transparent(size):
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    img.save('./transparent.png')
    return './transparent.png'

def get_links(_path_="/Layers/"):

    PATH = os.getcwd().replace('\\', '/')
    folders = os.listdir(f'{PATH}/{_path_}/')

    links = {}
    folder_path = []

    for folder in folders:

        items = os.listdir(f'{PATH}/Layers/{folder}')
        folder_path.append(f'{PATH}/Layers/{folder}')
        temp = []
        # print(folder)
        for item in items:
            # print(item)
            if item != "Thumbs.db":
                _path = f'{PATH}/Layers/{folder}/{item}'
                if os.path.exists(_path):
                    temp.append(_path)
        links[folder] = temp

    return links


def get_td():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    return dt_string


def create_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def init_log_count(count):  # To Initialize the logs.
    # t = f"{get_td()}"
    _path = os.getcwd().replace('\\', '/')
    path = f'{_path}/Logs/{count}_logs.csv'
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID", "Layer0", "Layer1", "Layer2", "Layer3", "Layer4", "Layer5", "Layer6",
            "Layer7", "Layer8", "Layer9"])
    return path


def init_log():  # To Initialize the logs.
    t = f"{get_td()}"
    _path = os.getcwd().replace('\\', '/')
    path = f'{_path}/Logs/{t}_logs.csv'
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "ID", "Layer0", "Layer1", "Layer2", "Layer3", "Layer4", "Layer5", "Layer6",
            "Layer7", "Layer8", "Layer9"])
    return path

def update_logs(log_path, value_list
                ):  # dict -> {'id':[-], 'face':[-],.....and other body parts }
    with open(log_path, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(value_list)


def logging_info(count, links):
    temp = []
    temp.append(count)
    for link in links:
        _link = link.split('/')[-1]
        _link_ = _link.split('.')[0].split("#")[0]
        temp.append(_link_)
    return temp

def get_attributes(links):
    temp = []
    for x in links:
        key = x.split("/")[-2].split('.')[-1]
        value = x.split("/")[-1].split('.')[0].split("#")[0]
        if key:
            temp.append({
                                "trait_type":key,
                                "value":str(value)
                            })
    return temp


def putting(images):

    for x, image in enumerate(images):
        if x == 0:
            bg = Image.open(image)
        else:
            fg = Image.open(image)
            bg.paste(fg, (0, 0), fg.convert("RGBA"))

    return bg


def resized(size, links):

    for link in tqdm(links):
        image = Image.open(link)
        res = image.resize(size, Image.LANCZOS)
        res.save(link)


def meta_json(json_name, public_dict):
    with open(f'./Metadata/{json_name}.json', "w") as outfile:
        json.dump(public_dict, outfile, indent=6)



def open_json(path):
    with open(path, 'r', encoding='utf-8') as openfile:
        # print(openfile)
        json_object = json.load(openfile)

    return json_object