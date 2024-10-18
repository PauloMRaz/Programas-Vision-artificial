import cv2
import numpy as np
import os

# Función para agregar ruido gaussiano a una imagen
def add_gaussian_noise(image, mean=0, std_dev=25):
    h, w, c = image.shape
    noise = np.random.normal(mean, std_dev, (h, w, c))
    noisy_image = np.clip(image + noise, 0, 255)
    return noisy_image.astype(np.uint8)

# Función para agregar ruido sal y pimienta a una imagen
def add_salt_and_pepper_noise(image, prob=0.05):
    noisy_image = np.copy(image)
    num_salt = np.ceil(prob * image.size * 0.5)
    salt_coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1], :] = 255

    num_pepper = np.ceil(prob * image.size * 0.5)
    pepper_coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0

    return noisy_image.astype(np.uint8)

# Función para aplicar diferentes filtros a una imagen
def apply_filters(image):
    gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)
    median_filtered = cv2.medianBlur(image, 5)
    mean_filtered = cv2.blur(image, (5, 5))
    min_filtered = cv2.erode(image, np.ones((3, 3), np.uint8))
    max_filtered = cv2.dilate(image, np.ones((3, 3), np.uint8))
    return [gaussian_filtered, median_filtered, mean_filtered, min_filtered, max_filtered]

# Función para mostrar varias imágenes con OpenCV
def show_images_with_cv2(images, titles):
    for img, title in zip(images, titles):
        cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cargar la imagen original
original_image = cv2.imread('Ladrillos.png')

# Contaminar la imagen original con ruido gaussiano y ruido sal y pimienta
noisy_gaussian_image = add_gaussian_noise(original_image)
noisy_salt_and_pepper_image = add_salt_and_pepper_noise(original_image)

# Crear un directorio para almacenar las imágenes contaminadas
os.makedirs("contaminated_images", exist_ok=True)

# Guardar las imágenes contaminadas como archivos PNG
cv2.imwrite("contaminated_images/noisy_gaussian.png", noisy_gaussian_image)
cv2.imwrite("contaminated_images/noisy_salt_and_pepper.png", noisy_salt_and_pepper_image)

# Mostrar las imágenes contaminadas con OpenCV
contaminated_titles = ['Noisy (Gaussian)', 'Noisy (Salt & Pepper)']
show_images_with_cv2([noisy_gaussian_image, noisy_salt_and_pepper_image], contaminated_titles)

# Aplicar filtros a las imágenes contaminadas
filtered_images_gaussian = apply_filters(noisy_gaussian_image)
filtered_images_salt_and_pepper = apply_filters(noisy_salt_and_pepper_image)

# Crear un directorio para almacenar las imágenes filtradas
os.makedirs("filtered_images", exist_ok=True)

# Guardar las imágenes filtradas como archivos PNG
for i, img in enumerate(filtered_images_gaussian):
    cv2.imwrite(f"filtered_images/gaussian_{i}.png", img)
for i, img in enumerate(filtered_images_salt_and_pepper):
    cv2.imwrite(f"filtered_images/salt_and_pepper_{i}.png", img)

# Mostrar las imágenes filtradas con OpenCV
filter_titles = ['Gaussian', 'Median', 'Mean', 'Minimum', 'Maximum']
show_images_with_cv2(filtered_images_gaussian, filter_titles)
show_images_with_cv2(filtered_images_salt_and_pepper, filter_titles)



