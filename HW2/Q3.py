import cv2
import numpy as np


def quantize_image(image_path):
    # 1. Read the image in Grayscale (8-bit)
    img = cv2.imread(image_path, 0)

    if img is None:
        print("Error: Could not load image. Check path.")
        return

    # 2. Perform Quantization (Reduce to 4-bit)
    # Bit shifting right by 4 divides the value by 16.
    # Values 0-255 become values 0-15.
    quantized_raw = img >> 4

    # 3. Scale back to 0-255 range for Visualization
    # back to the full intensity range (0-255).
    # Factor = 255 / 15 = 17
    quantized_display = (quantized_raw * 17).astype(np.uint8)

    # 4. Display the results
    cv2.imshow('Original (8-bit)', img)
    cv2.imshow('Quantized 4-bit (16 Levels)', quantized_display)

    print(f"Original Range: 0 to 255")
    print(f"Quantized Raw Values: {np.min(quantized_raw)} to {np.max(quantized_raw)}")
    print(f"Display Scaled Values: {np.min(quantized_display)} to {np.max(quantized_display)}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_file = 'grayscale_image.jpg'
    quantize_image(image_file)
