import json
from logger import *
from json import JSONDecodeError

POST_PATH = "posts.json"
REQUIREMENT_FORMAT = ['png', 'jpg', 'gif']


# Получение с JSON и поиск по постам
def loader_from_json(search_by):
    not_found_post = [{
            "pic": "http://pravkhabarovsk.ru/upload/information_system_1/3/1/5/item_31509/small_information_items_31509.jpg",
            "content": "Нет поста с таким описанием, поищи ещё! :)"
        }]
    try:
        with open(POST_PATH, 'r', encoding='UTF-8') as file:
            posts = json.load(file)
            find_post = [x for x in posts if search_by.lower() in x["content"].lower()]

        if len(find_post) >= 1:
            new_logger.info('Search complited!')
            return find_post
        else:
            new_logger.info("Post wasn't detected")
            return not_found_post

    except JSONDecodeError:
        new_logger.critical("JSON file doesn't exist or can't be decode")


# Проверка формата файла
def check_format_file(file_name):
    file_name_ = file_name.split('.')

    if file_name_[1] in REQUIREMENT_FORMAT:
        return True
    new_logger.critical('File not image!')
    return False


# Запись загруженного поста в JSON файл
def download_to_json(picture, content):
    try:
        new_data = {"pic": picture, "content": content}
        with open('posts.json', encoding='UTF-8') as file:
            data = json.load(file)
            data.append(new_data)
            with open('posts.json', 'w', encoding='UTF-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)

    except JSONDecodeError:
        new_logger.error("JSON file decode process was failed!")

    except FileNotFoundError:
        new_logger.error('JSON file didn\'t find!')
