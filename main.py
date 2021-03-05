from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import os
import time
import random
import string


IMG_ID = 'screenshot-image'
DOMEN = r'https://prnt.sc/'

class ImgParser():
  
    def __init__(self, url='aaaaa1', count=10):
        self.url = url
        self.count = count

    
    def get_next_url(self):
        list_url = list(self.url)
        list_index = []
        list_next_let = []
        for index, elem in enumerate(self.url):
            if 97 <= ord(elem) < 122:
                next_let = chr(ord(elem) + 1)
                list_next_let.append(next_let)
                list_index.append(index)
        list_url[min(list_index)] = list_next_let[0]
        next_url = ''.join(list_url)
        return next_url
  
  
    def save_image(self, image_url):
        
        name_image = self.url + os.path.splitext(image_url)[1]
        with open(name_image, 'wb') as image:
            image.write(image_url)
            
  

    
    
    def run(self):
        
        ua = UserAgent()
        headers = {'User-Agent':str(ua.random)}
        r = requests.get(DOMEN + self.url, headers=headers)
        for i in range(self.count):
            if r.status_code == 200:
                image = self.get_image(r.text)
                if image:
                  self.save_image(image)
                self.get_next_url()
            time.sleep(1)
                
           
              
    def get_image(self, text):
        soup = BeautifulSoup(text, "html.parser")
        if soup is not None:
            id_image = soup.find(id='screenshot-image')
            return id_image.src
        else:
            raise ValueError()
        

    def create():
        inp_url = input('Введите url')
        inp_count = input('Введите количество')
        created = ImgParser(inp_url, inp_count)
        created.run()
