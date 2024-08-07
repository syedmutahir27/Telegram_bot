import json
import os
import random
import requests
from dotenv import load_dotenv
load_dotenv()

def get_image(category,orientation):
    category= category.replace(" ","+")
    url=f"https://api.unsplash.com/search/photos?client_id={os.environ['ACCESS_KEY']}&page=1&query={category}&per_page=20&orientation={orientation}"
    response = requests.get(url)
    ext_dict = json.loads(response.text)
    results = ext_dict["results"]

    img_list = []
    for i in results :
        usr_dict ={}
        usr_dict['url']= i["urls"]["regular"]
        usr_dict['author']= i["user"]["username"]
        img_list.append((usr_dict))

    return random.choice(img_list)






