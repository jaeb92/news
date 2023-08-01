import os
import requests
from PIL import Image
from io import BytesIO

def save_img(image_urls: str, site: str, news_id: str):

    for image_url in image_urls:
        image_save_root = f'static/news_image/{site}/{news_id}'
        if not os.path.exists(image_save_root):
            os.makedirs(image_save_root, exist_ok=True)
        
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        # img.show() # 이미지 확인
        img.save(f'{image_save_root}/{image_url.split("/")[-1]}')