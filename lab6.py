import cv2
import numpy as np

img = cv2.imread('./lab10/img.JPG')

img = cv2.resize(img, (750, 500))

cv2.imwrite("bocian4.png", img) 

HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(HSV)

blur = cv2.blur(H,(60,60))



ret, thresh1 = cv2.threshold(blur, 140, 255, cv2.THRESH_BINARY) 

cv2.imshow('aa', thresh1)

result = cv2.bitwise_and(img, img, mask=thresh1)
result[thresh1==0] = [0,0,0]

cv2.imshow('thresh', result)
cv2.imwrite("bocian1.png", result) 
cv2.imwrite("bocian2.png", thresh1) 
cv2.imwrite("bocian3.png", H) 

while True:
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()