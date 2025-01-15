import cv2
import numpy as np
import sys
import math
import time


x_p = -1
y_p = -1

for i in range(51, 123):

    path = "./lab8/img/obrazki00"
    if i < 100:
        path += "0"

    path += str(i)
    path += ".jpg"
    img = cv2.imread(path)
    ret, thresh1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    x, y, z = np.where(thresh1==(255,255,255))
    if x_p == -1:
        x_p = x[0]
        y_p = y[0]

    txt = "X: " + str(y[0] - y_p) + " Y: " + str(x[0] - x_p)
    print(txt)

    x_p = x[0]
    y_p = y[0]

    cv2.imshow('aa', img)
    cv2.waitKey(33)
    



while True:
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()