import cv2


def crop_center_200x200(image_path):
    # 1. Read the image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Get image dimensions (Height, Width)
    h, w = img.shape[:2]

    # 3. Define the crop size
    crop_size = 200

    # 4. Error Handling: Check if image is large enough
    if w < crop_size or h < crop_size:
        print(f"Error: Image is too small ({w}x{h}) to crop a {crop_size}x{crop_size} region.")
        return

    # 5. Calculate start and end coordinates
    # Center coordinates
    center_x, center_y = w // 2, h // 2

    # Top-left corner (start)
    start_x = center_x - (crop_size // 2)
    start_y = center_y - (crop_size // 2)

    # Bottom-right corner (end)
    end_x = start_x + crop_size
    end_y = start_y + crop_size

    print(f"Cropping region from x:{start_x} to x:{end_x}, y:{start_y} to y:{end_y}")

    # 6. Crop using NumPy array slicing
    # Syntax: image[row_start:row_end, col_start:col_end]
    cropped_img = img[start_y:end_y, start_x:end_x]

    # 7. Display the results
    # Resize the window slightly just to make sure it's visible
    cv2.imshow('Original Image', img)
    cv2.imshow('Cropped 200x200 (Center)', cropped_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    crop_center_200x200('color_image.jpg')
