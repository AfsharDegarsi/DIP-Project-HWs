import cv2


def downsample_numpy(image_path):
    # 1. Read the image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Downsample by slicing
    # Syntax: array[start:stop:step]
    # [::2] means take every 2nd pixel starting from 0
    downsampled_img = img[::2, ::2, :]

    # 3. Display Info and Images
    h, w = img.shape[:2]
    nh, nw = downsampled_img.shape[:2]

    print(f"Original Size: {w}x{h}")
    print(f"DownSampled Size: {nw}x{nh}")

    cv2.imshow('Original', img)
    cv2.imshow('DownSampled', downsampled_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    downsample_numpy('grayscale_image.jpg')
