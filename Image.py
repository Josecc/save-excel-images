# Author: Jose Canahui

import urllib.request
import os

class Image():
    def __init__(self, imageURL):
        super().__init__()
        self.imageURL = imageURL
    def download(self):
        if not os.path.exists('./images/'):
            os.makedirs('./images/')
        urllib.request.urlretrieve(self.imageURL, "images/" + self.imageURL.split('/')[-1] + ".png")
