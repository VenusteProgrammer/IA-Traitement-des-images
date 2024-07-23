from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

#######I.1.
folder_path = "/home/venuste/Documents/Cours_Bac3_2023-2024/IA"
image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".jfif")
image_paths2 = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
images = []
new_size = (200, 200)
i=0
for img_path in image_paths2: 
    try:
        img = Image.open(img_path)
        img = img.resize(new_size)
        images.append(img)
        i+=1
        #print(f"L'image {img_path} a été chargée et redimensionnée avec succès.")
    except Exception as e:
        print(f"Erreur de chargement de l'image {img_path}: {e}")

#image_paths = ["ja.jpg", "jaav.jpg", "essaie.jpg", "intare.jpg", "windows.jpg","OIP.jfif"]


images = [Image.open(img_path).resize(new_size) for img_path in image_paths2]
if i>10:
    while(i%10!=0):
        i+=1
    i=int(i/10)
else:
    i=int(1)

plt.figure(figsize=(12, 8))
for j, img in enumerate(images):
    plt.subplot(i, 10, j+1)
    plt.imshow(img)
    plt.axis('off')
plt.show()

#######I.2.

img = images[2]
img_array = np.array(img)
print(f"Taille de l'image: {img_array.shape}") 

#print(f"Taille de l'image2: {images[2].size}")

pixels = list(images[2].getdata())
print(f"Quelques pixels de l'image: {pixels[:100]}")


#####II.1

# black and white
gray_images = [img.convert("L") for img in images]

# Affichage des images en niveaux de gris
plt.figure(figsize=(12, 8))
for j, img in enumerate(gray_images):
    plt.subplot(i, 10, j+1)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
plt.show()

######II.2

# Afficher la taille de l'une de ces images en niveaux de gris
img = gray_images[2]
img_array = np.array(img)
print(f"Taille de l'image en niveaux de gris: {img_array.shape}")

#####II.3

# Convertir les images en couleur noire
#black_images = [Image.new("RGB", img.size, "black") for img in images]
black_images = []
for img in images:
    img_array = np.array(img)
    black_img_array = img_array * 0  
    black_img = Image.fromarray(black_img_array.astype('uint8'))
    black_images.append(black_img)

# Affichage des images en couleur noire
plt.figure(figsize=(12, 8))
for j, img in enumerate(black_images):
    plt.subplot(i, 10, j+1)
    plt.imshow(img)
    plt.axis('off')
plt.show()


