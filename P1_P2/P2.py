import cv2
import numpy as np

imagen=cv2.imread("IR.png")
cv2.imshow("IR",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("IR.jpg",imagen)

imagenO1=imagen*0.2
imagenO1=imagenO1.astype(np.uint8)

cv2.imshow("IR01.jpg", imagenO1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("IR01_os.jpg", imagenO1)