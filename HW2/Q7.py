import cv2


def get_pixel_intensity(image_path, x, y):
    # 1. Read the image in Grayscale mode
    img = cv2.imread(image_path, 0)

    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Get image dimensions (Height = Rows, Width = Columns)
    height, width = img.shape

    # 3. Check if coordinates are within the image bounds
    if x < 0 or x >= width or y < 0 or y >= height:
        print(f"Error: Coordinates ({x}, {y}) are out of bounds.")
        print(f"Valid range: x (0 to {width - 1}), y (0 to {height - 1})")
        return

    # 4. Extract the Intensity
    # Access the pixel at row 'y' and column 'x'
    intensity_value = img[y, x]

    # 5. Print the result
    print(f"--- Pixel Info ---")
    print(f"Coordinates (x, y): ({x}, {y})")
    print(f"Intensity Value:    {intensity_value}")


if __name__ == "__main__":
    # Replace with your image path
    image_file = 'grayscale_image.jpg'

    # Define the coordinates you want to check
    target_x = 100
    target_y = 50

    get_pixel_intensity(image_file, target_x, target_y)
