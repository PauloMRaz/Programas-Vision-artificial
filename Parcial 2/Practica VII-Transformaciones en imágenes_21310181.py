import cv2
import numpy as np

# Función para trasladar una imagen
def translate(image, x, y):
    rows, cols, _ = image.shape
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    return translated_image

# Función para rotar una imagen
def rotate(image, angle):
    rows, cols, _ = image.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    return rotated_image

# Función para escalar una imagen
def scale(image, scale_factor):
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
    return scaled_image

# Función para recortar una región de interés de una imagen
def crop(image, x, y, width, height):
    cropped_image = image[y:y+height, x:x+width]
    return cropped_image

# Cargar la imagen de entrada
image = cv2.imread('Ladrillos.png')

# Trasladar la imagen
translated_image = translate(image, 50, 50)
cv2.imwrite("translated_image.png", translated_image)
cv2.imshow('Translated Image', translated_image)

# Rotar la imagen
rotated_image = rotate(image, 45)
cv2.imwrite("rotated_image.png", rotated_image)
cv2.imshow('Rotated Image', rotated_image)

# Escalar la imagen
scaled_image = scale(image, 1.5)
cv2.imwrite("scaled_image.png", scaled_image)
cv2.imshow('Scaled Image', scaled_image)

# Recortar una región de interés de la imagen
cropped_image = crop(image, 100, 100, 200, 200)
cv2.imwrite("cropped_image.png", cropped_image)
cv2.imshow('Cropped Image', cropped_image)

# Mostrar la imagen original
cv2.imshow('Original Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

