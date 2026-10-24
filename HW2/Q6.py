import cv2


def generate_negative(image_path):
    # 1. Read the image in Grayscale mode (0)
    original_img = cv2.imread(image_path, 0)

    if original_img is None:
        print("Error: Could not load image. Check the path.")
        return

    # 2. Generate the Negative
    # We subtract the image matrix from 255.
    # NumPy handles this operation element-wise for every pixel simultaneously.
    negative_img = 255 - original_img

    # 3. Display the results
    cv2.imshow('Original Grayscale', original_img)
    cv2.imshow('Negative Image', negative_img)

    # 4. Save the result
    cv2.imwrite('negative_output.jpg', negative_img)

    print("Negative image generated and saved as 'negative_output.jpg'")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    generate_negative('grayscale_image.jpg')
