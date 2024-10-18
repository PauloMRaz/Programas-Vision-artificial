import cv2

# Cargar la imagen de entrada
image = cv2.imread('Ladrillos.png')

# Verificar si la imagen se cargó correctamente
if image is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Operaciones lógicas
    image_and = cv2.bitwise_and(image, image)
    image_or = cv2.bitwise_or(image, image)
    image_not = cv2.bitwise_not(image)
    image_xor = cv2.bitwise_xor(image, image)

    # Guardar las imágenes resultantes en formato PNG
    cv2.imwrite("image_and.png", image_and)
    cv2.imwrite("image_or.png", image_or)
    cv2.imwrite("image_not.png", image_not)
    cv2.imwrite("image_xor.png", image_xor)

    # Mostrar las imágenes resultantes
    cv2.imshow('AND', image_and)
    cv2.imshow('OR', image_or)
    cv2.imshow('NOT', image_not)
    cv2.imshow('XOR', image_xor)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


