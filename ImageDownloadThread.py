from threading import Thread
from Image import Image

class ImageDownloadThread(Thread):
    def __init__(self, imageURLs):
        super().__init__()
        self.imageURLs = imageURLs

    def run(self):
        for imageURL in self.imageURLs:
            Image(imageURL).download()
