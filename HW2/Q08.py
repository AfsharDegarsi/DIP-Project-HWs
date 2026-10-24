import cv2


def extract_msb_plane(image_path):
    # 1. Read the image in Grayscale (8-bit)
    img = cv2.imread(image_path, 0)

    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Extract the MSB
    # Bitwise right shift by 7 positions.
    msb_binary = img >> 7

    # 3. Scale for Visualization
    # The values are currently 0 or 1, which would be invisible on a screen.
    # Multiply by 255 to map 0 -> 0 (Black) and 1 -> 255 (White).
    msb_visual = msb_binary * 255

    # 4. Display the results
    cv2.imshow('Original Image', img)
    cv2.imshow('MSB Plane (8th Bit)', msb_visual.astype('uint8'))

    print("Displaying Original Image and MSB Plane...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    extract_msb_plane('grayscale_image.jpg')
