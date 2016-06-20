# save-excel-images
A small python script to traverse an excel column for image urls and save them.

# Quick Start
You need:
* Python 3.4.*
* pandas python library
* This repo
* Excel file with image urls

You can find out which version of python 3 you're running by executing in the command line `$ python3 --version`.

To clone this repo simply make sure you have git installed and run `$ git clone https://github.com/Josecc/save-excel-images.git`.

Lastly, you need to provide the name of the excel file as an argument to this program. Additionally, you can provide a second argument that states what column the urls are in, and one more to specify the number of concurrent downloads (defaults to 3) Ex. `$ python3 SaveExcelImages.py example.xlsx img_url 3`.
