import cv2
import numpy as np


def analyze_image(file_path):
    # Read the image
    # The second argument, 0, or cv2.IMREAD_GRAYSCALE, converts the image to grayscale upon loading
    img = cv2.imread(file_path, 0)

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Unable to load image. Please check the file path.")
        return

    print("--- Image Properties ---")

    # 1. Display Size
    # The shape attribute returns a tuple (height, width) for a grayscale image
    height, width = img.shape
    print(f"Size (Height x Width): {height} x {width}")

    # 2. Display Data Type
    print(f"Data Type: {img.dtype}")

    # 3. Display Intensity Range
    # np.min and np.max find the darkest and lightest pixel values
    min_val = np.min(img)
    max_val = np.max(img)
    print(f"Intensity Range: {min_val} to {max_val}")


if __name__ == "__main__":
    image_path = 'grayscale_image.jpg'

    analyze_image(image_path)
