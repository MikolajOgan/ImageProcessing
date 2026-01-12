# ImageProcessing

| File | Description                                                                                                                                                                      |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lab1 | Loads a grayscale image from a CLI path, asks for a (2n+1)×(2n+1)(2n+1)\\times(2n+1)(2n+1)×(2n+1) kernel from stdin, applies cv2.filter2D, and displays the result.              |
| lab2 | Crops a region from ./lab2/img.jpg and compares multiple thresholding methods: binary, to-zero, Otsu, and adaptive mean.                                                         |
| lab3 | Detects lines with Canny + Hough transform, rotates the image using the detected angle, then finds contours and crops the rotated result before saving.                          |
| lab4 | Runs corner detection (goodFeaturesToTrack) on an image and on two rotated versions, drawing corner points and saving outputs.                                                   |
| lab5 | Iterates through an image sequence (./lab8/img/obrazki00XX.jpg), thresholds for white pixels, and prints frame-to-frame movement (ΔX/ΔY) based on the first detected white pixel.|
| lab6 | Converts an image to HSV, thresholds the Hue channel after blurring, and uses the mask to segment the image.                                                                     |
| lab7 | Computes and plots the grayscale histogram before and after histogram equalization.                                                                                              |
