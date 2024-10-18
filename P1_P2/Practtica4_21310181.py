#Paulo Enrique Muñoz Razón      21310181      
#Practica 4                11/03/2024
#Vision Artificial 

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def clasificador(imagen):
  m,n,c=imagen.shape
  imagenr=np.zeros((m,n))
  for x in range(m):
      for y in range(n):
          if 20<= imagen[x,y,0] <= 80 and 20 < imagen[x,y,1] <=95 and 33 < imagen[x,y,2] <=160 :
             imagenr[x,y]=225
  imagenr = imagenr.astype(np.uint8)
  return imagenr

def clasificador2(imblan):
  m,n,c=imagen.shape
  imagent=np.zeros((m,n))
  for x in range(m):
      for y in range(n):
          if 20<= imblan[x,y,0] <= 95 and 20 < imblan[x,y,1] <=125 and 33 < imblan[x,y,2] <=190 :
             imagent[x,y]=225
  imagent = imagent.astype(np.uint8)
  return imagent

def adaptador(imagen):
    imagenc=imagen
    m,n,c  = imagen.shape
    imagenc= imagen.astype(float)
    imblan = np.zeros((m,n,c))
    b=np.max(imagenc[:,:,0])
    g=np.max(imagenc[:,:,1])
    r=np.max(imagenc[:,:,2])
    for x in range(m):
       for y in range(n):
             imblan[x,y,0]=(255/b)*imagenc[x,y,0]
             imblan[x,y,1]=(255/g)*imagenc[x,y,1]
             imblan[x,y,2]=(255/r)*imagenc[x,y,2]      
    imblan = imblan.astype(np.uint8)
    
    return imblan


def imprimir(imagen,imagen2,imagen3,imagen4,q,a,w,s,z,x,e,d,r,f,v,t) :
    i1=cv2.resize(imagen,  (269,97), interpolation=cv2.INTER_CUBIC)
    i2=cv2.resize(imagen2,  (269,97), interpolation=cv2.INTER_CUBIC)
    i3=cv2.resize(imagen3,  (269,97), interpolation=cv2.INTER_CUBIC)
    i4=cv2.resize(imagen4,  (269,97), interpolation=cv2.INTER_CUBIC)
    
    i11=cv2.resize(r,  (269,97), interpolation=cv2.INTER_CUBIC)
    i22=cv2.resize(f,  (269,97), interpolation=cv2.INTER_CUBIC)
    i33=cv2.resize(v,  (269,97), interpolation=cv2.INTER_CUBIC)
    i44=cv2.resize(t,  (269,97), interpolation=cv2.INTER_CUBIC)
    
    i1_=cv2.resize(q,  (269,97), interpolation=cv2.INTER_CUBIC)
    i2_=cv2.resize(w,  (269,97), interpolation=cv2.INTER_CUBIC)
    i3_=cv2.resize(z,  (269,97), interpolation=cv2.INTER_CUBIC)
    i4_=cv2.resize(e,  (269,97), interpolation=cv2.INTER_CUBIC)
    
    concat_h = cv2.hconcat([i1,i2,i3,i4])
    concat_h2 = cv2.hconcat([i11,i22,i33,i44])
    concat_h3 = cv2.hconcat([i1_,i2_,i3_,i4_])
    concat_h4 = cv2.hconcat([a,s,x,d])
    cv2.imshow("Todas las manos en una sola",concat_h)
    cv2.imshow("Manos en croma",concat_h2)
    cv2.imshow("Manos originales",concat_h3)
    cv2.imshow("Manos en blanco y negro",concat_h4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imagen=cv2.imread ("imagen-OG.jpeg")
imagen2=cv2.imread ("imagen-rosa.jpeg")
imagen3=cv2.imread ("imagen-verde.jpeg")
imagen4=cv2.imread ("imagen-violeta.jpeg")

imagenr=clasificador(imagen)
imblan=adaptador(imagen)
imagent=clasificador2(imblan)
q=imblan
a=imagent 
r=imagenr

imagenr=clasificador(imagen2)
imblan=adaptador(imagen)
imagent=clasificador2(imblan)
w=imblan
s=imagent 
f=imagenr

imagenr=clasificador(imagen3)
imblan=adaptador(imagen)
imagent=clasificador2(imblan)
z=imblan
x=imagent 
v=imagenr

imagenr=clasificador(imagen4)
imblan=adaptador(imagen)
imagent=clasificador2(imblan)
e=imblan
d=imagent 
t=imagenr

imprimir(imagen,imagen2,imagen3,imagen4,q,a,w,s,z,x,e,d,r,f,v,t)