import numpy as np
import cv2 
 
img = cv2.imread('Ladrillos.png',0)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv2.Canny(img,100,200)
 
cv2.imshow("ladrilloCanny", edges)
cv2.waitKey()
cv2.destroyAllWindows()

