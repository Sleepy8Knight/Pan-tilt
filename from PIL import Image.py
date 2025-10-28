from PIL import Image

import pytesseract

import cv2

import os, sys, inspect #For dynamic filepaths

import numpy as np;	



cam = cv2.VideoCapture(0)



while True:

    check, frame = cam.read()
    img = cv2.resize(frame,(320,240))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
 
    




    img_empty = np.zeros((img.shape[0], img.shape[1]))

    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)

    img3 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    img4 = cv2.GaussianBlur(img3, (3, 3), 0)

    text = pytesseract.image_to_string(img4)



    # Output

    cv2.imshow("Original", img)

    #cv2.imshow("Normalized", img2)

    cv2.imshow("Threshold", img3)

    cv2.imshow("Blurred", img4)

    print(text)

    

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()