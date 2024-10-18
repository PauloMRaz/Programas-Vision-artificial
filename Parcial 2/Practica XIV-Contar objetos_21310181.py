import cv2
import numpy as np

def encontrar_contornos(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Filtrar la imagen para eliminar el ruido (opcional, dependiendo del caso)
    gris_filtrado = cv2.GaussianBlur(gris, (5, 5), 0)

    # Aplicar el detector de bordes Canny
    bordes = cv2.Canny(gris_filtrado, 30, 150)

    # Buscar los contornos en los bordes detectados
    contornos, _ = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos encontrados en una copia de la imagen original
    contornos_dibujados = imagen.copy()
    cv2.drawContours(contornos_dibujados, contornos, -1, (0, 255, 0), 2)

    return contornos_dibujados

# Cargar la imagen
imagen = cv2.imread('Ladrillos.png')

# Encontrar contornos en la imagen
imagen_con_contornos = encontrar_contornos(imagen)

# Mostrar la imagen original y la imagen con los contornos dibujados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Contornos', imagen_con_contornos)
cv2.waitKey(0)
cv2.destroyAllWindows()


