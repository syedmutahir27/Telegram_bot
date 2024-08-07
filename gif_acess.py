import json
import random
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def get_gif(category):
    lmt = 10
    url=f"https://tenor.googleapis.com/v2/search?q={category}&key={os.environ['TENOR_API_KEY']}&client_key='wallpy'&limit={lmt}"
    response = requests.get(url)
    ext_dict = json.loads(response.text)
    results = ext_dict["results"]

    img_list = []
    for i in results:
        usr_dict = {}
        usr_dict['url'] = i["media_formats"]["gif"]["url"]
        img_list.append((usr_dict))

    return random.choice(img_list)





if __name__ == '__main__':
    get_gif("excited")




