#Paulo Enrique Muñoz Razón      21310181      
#Practica 4                11/03/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import cv2
import numpy as np

imagen=cv2.imread("IR.jpg")
imagen1=imagen.copy()
imagen2=imagen.copy()
imagen3=imagen.copy()
imagen1[:,:,0]=imagen[:,:,0]+20
imagen2[:,:,1]=imagen[:,:,1]+50
imagen3[:,:,2]=imagen[:,:,2]+60

def whitepatch(imagen):
    m,n,c=imagen.shape
    imagenc=imagen.copy()
    imagen=imagen.astype(np.float32)
    imagenc=imagenc.astype(np.float32)
    for x in range(m):
        for y in range(n):
            imagenc[x,y,0]=imagen[x,y,0]*(255/np.max(imagen[:,:,0]))
            imagenc[x,y,1]=imagen[x,y,1]*(255/np.max(imagen[:,:,1]))
            imagenc[x,y,2]=imagen[x,y,2]*(255/np.max(imagen[:,:,2]))
    
    imagenc=imagenc.astype(np.uint8)
    cv2.imshow("IR4", imagenc)
    cv2.waitKey()
    cv2.destroyAllWindows()
    

cv2.imshow("IR1", imagen1)
cv2.imshow("IR2", imagen2)
cv2.imshow("IR3", imagen3)
cv2.waitKey()
cv2.destroyAllWindows()

whitepatch(imagen1)
whitepatch(imagen2)
whitepatch(imagen3)
