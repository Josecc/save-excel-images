# Author: Jose Canahui

import pandas as pd
import os.path

class Excel():
    def __init__(self, fileName):
        super().__init__()
        self.fileName = self.__getFile(fileName)

    def read(self, columnName=None):
        df = pd.read_excel(self.fileName)
        if columnName is None:
            imageURLs = df.as_matrix()
        else:
            imageURLs = df[columnName].tolist()
        if self.__checkString(imageURLs):
            return imageURLs

    def __getFile(self, fileName):
        if os.path.isfile(fileName):
            return fileName
        elif os.path.isfile(fileName + ".xlsx"):
            return (fileName + ".xlsx")
        else:
            print("File {} does not exist.".format(fileName))
            exit(1)

    def __checkString(self, imageURLs):
        if isinstance(imageURLs[0], str):
            return True
        else:
            print("Looks like the file has multiple columns, please specify the column to use.")
            exit(0)
