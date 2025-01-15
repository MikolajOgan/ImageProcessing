import cv2

img = cv2.imread('./lab2/img.jpg', cv2.IMREAD_GRAYSCALE)



cropped_image = img[150:200, 40:650]

ret, thresh1 = cv2.threshold(cropped_image, 120, 255, cv2.THRESH_BINARY) 
ret, thresh2 = cv2.threshold(cropped_image, 120, 255, cv2.THRESH_TOZERO)
ret, thresh3 = cv2.threshold(cropped_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 

thresh4 = cv2.adaptiveThreshold(cropped_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)


cv2.imshow('Cropped image', cropped_image)

cv2.imshow('THRESH_BINARY', thresh1)

cv2.imshow('THRESH_TOZERO', thresh2)

cv2.imshow('THRESH_OTSU', thresh3)

cv2.imshow('ADAPTIVE_THRESH_MEAN_C', thresh4)



while True:
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()