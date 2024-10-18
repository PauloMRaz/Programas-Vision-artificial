import cv2

imagen=cv2.imread("IR.jpg")
cv2.imshow("IR",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("IR.jpg",imagen)
