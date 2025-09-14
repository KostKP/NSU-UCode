import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import io

# === Константы === #
INVERT_MAX_VALUE = 255
DEFAULT_FIGSIZE = (10, 8)

# === Функции === #
def invert_image(image: np.ndarray) -> np.ndarray:
    """Инвертирует изображение (серое или RGB)."""
    return INVERT_MAX_VALUE - image

def load_image_with_fallback(loader_func, fallback_path: str) -> np.ndarray:
    """
    Загружает изображение с помощью функции loader_func.
    Если не удалось, пробует загрузить из fallback_path.
    """
    try:
        return loader_func()
    except Exception:
        print(f"[!] skimage.data недоступен, загружаю из {fallback_path}")
        return io.imread(fallback_path)

def plot_comparison(images: list, titles: list, figsize: tuple = None):
    """
    Универсальная функция для отрисовки изображений.
    Размер фигуры выбирается автоматически, если figsize не задан.
    """
    n = len(images)
    cols = 2
    rows = (n + 1) // 2

    # Если не задан размер — делаем адаптивный
    if figsize is None:
        figsize = (cols * 5, rows * 4)

    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.ravel()

    for i, (img, title) in enumerate(zip(images, titles)):
        if img.ndim == 2:  # серое изображение
            axes[i].imshow(img, cmap="gray")
        else:  # цветное
            axes[i].imshow(img)
        axes[i].set_title(title)
        axes[i].axis("off")

    # Убираем лишние оси, если картинок меньше
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    plt.show()

# === Основной сценарий === #
def main():
    gray_image = load_image_with_fallback(data.camera, "camera.png")
    rgb_image = load_image_with_fallback(data.astronaut, "astronaut.png")

    gray_inverted = invert_image(gray_image)
    rgb_inverted = invert_image(rgb_image)

    images = [gray_image, gray_inverted, rgb_image, rgb_inverted]
    titles = ["Исходное (Gray)", "Инвертированное (Gray)",
              "Исходное (RGB)", "Инвертированное (RGB)"]

    plot_comparison(images, titles)

if __name__ == "__main__":
    main()
