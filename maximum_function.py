'''This is a simple program that carries out the following process:
1. importing random module used to get random value for a given range
2. importing urllib modolue and using the request module to get url from the web
and also read the url
3. A function to carry out 1,2 and also to open a image file on a local system
'''


import random
from urllib import request
#from PIL import Image


def download_img(url):
    name = random.randrange(1, 1000)
    f_name = 'newimage' + str(name) + ".jpg"
    r = request.urlopen(url).read()
    with open(f_name, 'wb') as f:
        f.write(r)
    
    
    
    

download_img('https://ae01.alicdn.com/kf/HTB11DrjfgjN8KJjSZFgq6zjbVXa0/Background-Vinyl-Photography-Backdrops-City-Views-Computer-Printed-Backdrop-for-Photo-Studio-Baby-Newborn-Children.jpg')
