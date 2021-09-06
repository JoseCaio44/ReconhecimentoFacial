import cv2
import numpy as np

image = cv2.imread('caio.jpg', 0)
equalization = cv2.equalizeHist(image)
result = np.hstack((image,equalization))

cv2.imshow('caio.jpg',result)

cv2.imwrite('caio_normalizado.jpg',result)

#cv2.waitKey(0) 
#cv2.destroyAllWindows() 