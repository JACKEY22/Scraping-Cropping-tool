#Cropping_crosswalk.py
import cv2 as cv 
import numpy as np
import os

def make_canny(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(3,3),0)
    canny = cv.Canny(blur,150,300)
    return canny   

def make_binary(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3,3), 0)
    ret, binary = cv.threshold(blur, 200, 255, 0)
    return binary

cwd = os.getcwd()
dir = cwd + '/crosswalk/'
dir_crop = dir + 'crop/'
crosswalks = os.listdir(dir)


for crosswalk in crosswalks:
    crosswalk_num = crosswalk.split('.')[0]

    image = cv.imread(dir + f'/{crosswalk}')
    canny = make_canny(image)
    binary = make_binary(image)
    

    cv.imshow("canny", canny)
    cv.imshow("binary", binary)    
    cv.waitKey(0)