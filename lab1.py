import cv2
import os
import sys
import numpy as np

path = sys.argv[1]

img = cv2.imread(os.path.dirname(__file__) + '/' + path, cv2.IMREAD_GRAYSCALE)

def load_square_matrix():
    n = int(input("Enter n to get the size of the square matrix (2n+1). n="))
    n = n*2 + 1
    matrix = np.zeros((n, n), dtype=float)
    print("Enter the elements row-wise (2 3 4 ...):")

    for i in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            print("Error: Each row must have exactly", n, "elements. Please re-enter the row.")
            return load_square_matrix()
        matrix[i] = row

    return matrix

matrix = load_square_matrix()
for row in matrix:
        print(row)

img = cv2.filter2D(src=img, ddepth=-1, kernel=matrix) 

cv2.imshow('baboon', img)

while True:
    if cv2.waitKey(0) == 27:
        break
    cv2.destroyAllWindows()
