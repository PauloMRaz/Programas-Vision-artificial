import cv2
import numpy as np
imagen=cv2.imread("Ladrillos.png",0)



kernel=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

filtrada=np.zeros_like(imagen)
m,n=imagen.shape

imagen[0:3,0:3]*kernel

for x in range(m-2):
    for y in range(n-2):
        res=np.sum(imagen[x:x+3,y:y+3]*kernel)
        if abs(res)>100:
            filtrada[x,y]=250
            
            
cv2.imshow("imagen original", imagen)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("imagen filtrada", filtrada)
cv2.waitKey()
cv2.destroyAllWindows()