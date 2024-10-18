#Paulo Enrique Muñoz Razón      21310181      
#Practica 3                11/03/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import cv2
import numpy as np

imagen=cv2.imread("IR.jpg")
imagen1=imagen*0.8
imagen2=imagen*0.5

m,n,c=imagen.shape
imagenc=imagen.copy()
imagen=imagen.astype(np.float32)
imagenc=imagenc.astype(np.float32)

for x in range(m):
    for y in range(n):
        imagenc[x,y,0]=imagen[x,y,0]/(imagen[x,y,0] + imagen[x,y,1] + imagen[x,y,2])
        imagenc[x,y,1]=imagen[x,y,1]/(imagen[x,y,0] + imagen[x,y,1] + imagen[x,y,2])
        imagenc[x,y,2]=imagen[x,y,2]/(imagen[x,y,0] + imagen[x,y,1] + imagen[x,y,2])


cv2.imshow("IR", imagenc)
cv2.waitKey()
cv2.destroyAllWindows()