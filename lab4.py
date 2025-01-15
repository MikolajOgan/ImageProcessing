import cv2
import numpy as np
import sys
import math

img = cv2.imread('./lab7/rynek_frag.JPG', cv2.IMREAD_GRAYSCALE)

imgc = cv2.imread('./lab7/rynek_frag.JPG')

img = cv2.resize(img, (750, 500))

imgc = cv2.resize(imgc, (750, 500))

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

rotated = rotate_image(img, -56)
rotatedc = rotate_image(imgc, -56)

rotated2 = rotate_image(img, 36)
rotated2c = rotate_image(imgc, 36)

def detect(img, imgc):
  corners = cv2.goodFeaturesToTrack(img, 100, 0.01, 10) 
    
  corners = np.int0(corners)
    
  for i in corners: 
      x, y = i.ravel() 
      cv2.circle(imgc, (x, y), 3, (255, 0, 0), -1)

  return imgc

img1 = detect(img, imgc)
img2 = detect(rotated, rotatedc)
img3 = detect(rotated2, rotated2c)

cv2.imshow('aa', img1)
cv2.imwrite("bocian3.png", img1) 

cv2.imshow('aav', img2)
cv2.imwrite("bocian2.png", img2) 


cv2.imshow('aasv', img3)
cv2.imwrite("bocian1.png", img3) 

while True:
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()