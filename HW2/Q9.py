import cv2
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def plot_grayscale_histogram(image_path):
    # 1. Read the image in Grayscale
    img = cv2.imread(image_path, 0)

    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Calculate the histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    # 3. Plot the histogram
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist, color='black')
    plt.xlim([0, 256])
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    plot_grayscale_histogram('grayscale_image.jpg')
