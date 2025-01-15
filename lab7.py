import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./lab11/img.jpg', cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (750, 500))

hst = cv2.calcHist([img], [0], None, [256], [0,256])
hst2 = cv2.equalizeHist(img)
hst2 = cv2.calcHist([hst2], [0], None, [256], [0,256])

plt.figure()
plt.plot(hst)
plt.title('Original Image Histogram')

plt.figure()
plt.plot(hst2)
plt.title('Equalized Image Histogram')
plt.show()

cv2.imshow('baboon', img)

while True:
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()
