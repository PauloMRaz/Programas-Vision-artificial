#Paulo Enrique Muñoz Razón      21310181      
#Practica 5              11/03/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def clasificador(imagen):
  m,n,c=imagen.shape
  imagent=np.zeros((m,n))
  for x in range(m):
      for y in range(n):
          if 30 <= imagen[x,y,0] <= 120 and 200 < imagen[x,y,1] <=245 and 210 < imagen[x,y,2] <=254 :
             imagent[x,y]=225
  imagent = imagent.astype(np.uint8)
  return imagent
  
def mostrar(imagen):
    
    cv2.imshow("in",imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def etiquetado(imagent):
    num_labels,labels,stats,centroides = cv2.connectedComponentsWithStats(imagent,3,cv2.CV_32S)
    return num_labels,labels,stats,centroides
    
imagen=cv2.imread ("trespatos.jpg")
mostrar(imagen)
imagent = clasificador(imagen)
mostrar(imagent)

etiqueta=imagent
num_labels,labels,stats,centroides = cv2.connectedComponentsWithStats(etiqueta,3,cv2.CV_32S)
#descartamos el fondo y aislamos 
valor_max_pi = (np.max(stats[:4][1:]))/2 #asignamos el rango 
pin = np.where((stats[:,4][1:]) > valor_max_pi)
pin = pin[0]+1
mascaras = []
mascarafinal = 0 

for i in range (0, len(pin)):
    mascara = pin[i] == labels
    mascaras.append(mascara) 
    mascarasfinal = mascarafinal + mascaras[i]2d 
cv2.rectangle(imagen, (325,4),(600,250),(255,0,0),2)
cv2.rectangle(imagen, (420,280),(720,530),(255,0,0),2)
cv2.rectangle(imagen, (50,180),(350,460),(255,0,0),2)

imagen= cv2.resize(imagen,  (650,650), interpolation=cv2.INTER_CUBIC)

cv2.imshow("in",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()