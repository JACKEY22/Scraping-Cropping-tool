#Crop_using_mouse.py

import cv2 as cv

isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue, red = (255, 0, 0), (0, 0, 255)
 
def Crop(event, x, y, flags, param):
    global isDragging, x0, y0, img
    if event == cv.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv.EVENT_MOUSEMOVE:
        if isDragging:
            drawing = image.copy()
            cv.rectangle(drawing, (x0, y0), (x, y), blue, 2)
            cv.imshow('image', drawing)
    elif event == cv.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x - x0
            h = y - y0
            if w > 0 and h > 0:
                drawing = image.copy()
                cv.rectangle(drawing, (x0, y0), (x, y), red, 2)
                cv.imshow('image', drawing)
                crop = image[y0:y0+h, x0:x0+w]
                cv.imshow('cropped', crop)
                cv.moveWindow('cropped', 0, 0)
                cv.imwrite('./cropped.png', crop)
            else:
                cv.imshow('image', image)
                print('drag should start from left-top side')
 
image = cv.imread("crosswalk.jpg")
cv.imshow('image', image)
cv.setMouseCallback('image', Crop)
cv.waitKey()
cv.destroyAllWindows()

