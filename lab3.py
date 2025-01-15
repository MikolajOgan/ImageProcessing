import cv2
import numpy as np
import sys
import math

img = cv2.imread('./lab6/img.JPG')

img2 = cv2.resize(img, (750, 500))

blur = cv2.blur(img2,(10,10))

ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY) 
 
dst = cv2.Canny(thresh1, 50, 200, None, 3)

lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
 
if lines is not None:
 for i in range(0, len(lines)):
    rho = lines[i][0][0]
    theta = lines[i][0][1]
    a = math.cos(theta)
    b = math.sin(theta)
    x0 = a * rho
    y0 = b * rho
    pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
    pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
#cv2.line(img2, pt1, pt2, (0,0,120), 3, cv2.LINE_AA)

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

rotated = rotate_image(img2, -theta)

dstr = rotate_image(dst, -theta)

contours, hierarchy = cv2.findContours(dstr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

c = contours[0]
bottommost = tuple(c[c[:, :, 1].argmax()][0])[1] - 30

im = rotated[:bottommost, :]

cv2.imshow('aa', im)
cv2.imwrite("bocian1.png", im) 

while True:
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()