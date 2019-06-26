import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def segment1(img):    
    img = cv2.medianBlur(img,5)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    return th3

import os
directory_in_str = ["database/" , "query/"]
for d in directory_in_str:
    processed = d+"processed/"
    directory = os.fsencode(d)
    for file in os.listdir(d):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"): 
            path = os.path.join(d, filename)
            print(path)
            img = cv2.imread(path,0)
            img = segment1(img)
            cv2.imwrite(processed + filename, img)
#             cv2.imshow('image',img)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()

# import os
directory_in_str = ["database/processed/"]
# for d in directory_in_str:
#     processed = d+"processed/"
#     directory = os.fsencode(d)
#     for file in os.listdir(d):
#         filename = os.fsdecode(file)
#         if filename.endswith(".jpg"): 
#             path = os.path.join(d, filename)
#             print(path)
#             img = cv2.imread(path,0)
#             img = segment1(img)
#             cv2.imwrite(processed + filename, img)
import mahotas

with open("zernike.txt" ,"w") as txt:
    for d in directory_in_str:
        directory = os.fsencode(d)
        for file in os.listdir(d):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg"): 
                path = os.path.join(d, filename)
#                 print(path)
                img = cv2.imread(path,0)
                txt.write(str([i for i in mahotas.features.zernike_moments(img,10)])+"\n")

