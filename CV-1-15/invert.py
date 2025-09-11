import numpy as np
import matplotlib.pyplot as plt
from skimage import data

# Серое изображение
gray_image = data.camera()
gray_inverted = 255 - gray_image

# Цветное изображение (RGB)
rgb_image = data.astronaut()
rgb_inverted = 255 - rgb_image

# Визуализация
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
ax = axes.ravel()

ax[0].imshow(gray_image, cmap='gray')
ax[0].set_title("Исходное (Gray)")
ax[0].axis('off')

ax[1].imshow(gray_inverted, cmap='gray')
ax[1].set_title("Инвертированное (Gray)")
ax[1].axis('off')

ax[2].imshow(rgb_image)
ax[2].set_title("Исходное (RGB)")
ax[2].axis('off')

ax[3].imshow(rgb_inverted)
ax[3].set_title("Инвертированное (RGB)")
ax[3].axis('off')

plt.tight_layout()
plt.show()
