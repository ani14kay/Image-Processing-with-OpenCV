import cv2
img = cv2.imread('AK-PP.png',0)
cv2.imshow('Grayscale Image', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()