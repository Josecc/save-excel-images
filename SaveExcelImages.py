from ImageDownloadThread import ImageDownloadThread
from Excel import Excel

import numpy as np
import time
import sys

if len(sys.argv) == 2:
    excelImageURLs = Excel(sys.argv[1]).read()
    concurrentJobs = 3
elif len(sys.argv) == 3:
    excelImageURLs = Excel(sys.argv[1]).read(sys.argv[2])
    concurrentJobs = 3
else:
    excelImageURLs = Excel(sys.argv[1]).read(sys.argv[2])
    concurrentJobs = int(sys.argv[3])

print('Image URLs captured, downloading {:d} images at a time.'.format(concurrentJobs))

start = time.time()
threads = []

jobs = np.array_split(excelImageURLs, concurrentJobs)


for imageURLs in jobs:
    thread = ImageDownloadThread(imageURLs)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()

print('{:d} images downloaded in {:.3f} seconds.'.format(len(excelImageURLs), (end - start)))
