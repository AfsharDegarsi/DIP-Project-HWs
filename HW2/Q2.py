import cv2

# 1. Read the image
# OpenCV reads images in BGR format by default, not RGB
input_path = 'color_image.jpg'
image = cv2.imread(input_path)

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # 2. Convert BGR to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Display the results
    cv2.imshow('Original Color Image', image)
    cv2.imshow('Grayscale Image', gray_image)

    # 4. Save the grayscale image
    cv2.imwrite('grayscale_output.jpg', gray_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
