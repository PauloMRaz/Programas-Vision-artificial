import cv2
import numpy as np

# Cargar la imagen de entrada
image = cv2.imread('Ladrillos.png', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se cargó correctamente
if image is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Filtros Prewitt
    prewitt_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    prewitt_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    prewitt = cv2.magnitude(prewitt_x, prewitt_y)

    # Filtros Sobel
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobel_x, sobel_y)

    # Filtros Roberts
    roberts_x = cv2.filter2D(image, cv2.CV_64F, np.array([[1, 0], [0, -1]]))
    roberts_y = cv2.filter2D(image, cv2.CV_64F, np.array([[0, 1], [-1, 0]]))
    roberts = cv2.magnitude(roberts_x, roberts_y)

    # Escalar las imágenes para mostrarlas correctamente
    prewitt_display = cv2.normalize(prewitt, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    sobel_display = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    roberts_display = cv2.normalize(roberts, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Guardar las imágenes resultantes en formato PNG
    cv2.imwrite("prewitt.png", prewitt_display)
    cv2.imwrite("sobel.png", sobel_display)
    cv2.imwrite("roberts.png", roberts_display)

    # Mostrar las imágenes resultantes
    cv2.imshow('Prewitt', prewitt_display)
    cv2.imshow('Sobel', sobel_display)
    cv2.imshow('Roberts', roberts_display)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
