import cv2


def upsample_image(image_path):
    # 1. Read the image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Upsample by a factor of 2
    # We use None for the dsize (destination size) because we are defining the scale factors instead.
    # fx and fy are the scale factors along the horizontal and vertical axis.
    # interpolation=cv2.INTER_CUBIC is generally best for upsampling as it produces smoother results.
    upsampled_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # 3. Display dimensions
    h, w = img.shape[:2]
    uh, uw = upsampled_img.shape[:2]

    print(f"Original Size: {w} x {h}")
    print(f"Upsampled Size: {uw} x {uh}")

    # 4. Display the results
    cv2.imshow('Original Image', img)
    cv2.imshow('Upsampled Image (2x)', upsampled_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    upsample_image('grayscale_image_1.jpg')
