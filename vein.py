import numpy as np
import cv2

def multi_clahe(img, num):
    for i in range(num):
        img = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(4+i*2,4+i*2)).apply(img)
    return img

img = cv2.imread('4.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

final = multi_clahe(gray, 4)

cv2.imwrite('image.png',final)
cv2.imshow('image',final)

cv2.waitKey(0)
cv2.destroyAllWindows()