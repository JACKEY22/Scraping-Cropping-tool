#Cropping_sign.py
import cv2 as cv 
import numpy as np
import os

def make_binary(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3,3), 0)
    ret, binary = cv.threshold(blur, 200, 255, 0)
    return binary
    
def get_approx(contour):
    epsilon = 0.025*cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    return approx

def main():

    cwd = os.getcwd()
    dir = cwd + '/circle red sign/'
    dir_crop = dir + 'crop/'
    signs = os.listdir(dir)

    try:
        for sign in signs:
            sign_num = sign.split('.')[0]

            image = cv.imread(dir + f'/{sign}')
            binary = make_binary(image)

            contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                x,y,w,h = cv.boundingRect(contour)
                approx = get_approx(contour)

                if len(approx) > 6 and w > 100:
                    if not os.path.exists(dir_crop):
                        os.mkdir(dir_crop)
                    # cv.drawContours(image, [approx], 0, (255,0,0), -1)
                    crop = image[y:y+h,x:x+w]
                    cv.imwrite(dir_crop + f"{sign_num}_crop.jpg",crop)
    except:
        os.remove(dir + sign)
        print("deleted")

main()