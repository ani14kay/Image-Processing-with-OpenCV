from ctypes.wintypes import RGB
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('AK-PP.png')
#cv2.imshow('Original',img)
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale',grayImage)
cv2.waitKey(0) 
cv2.destroyAllWindows()