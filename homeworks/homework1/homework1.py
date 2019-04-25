import numpy as np
import cv2


def stretch_contrast(v, params):

    letters = [0] + params[0] + [256]
    coefs = [1] + params[1]
    ys = [0] + params[2] + [256]
    new = v
    for i in range(0, len(coefs) - 1):
        new = np.where(
            np.logical_and(v >= letters[i], v < letters[i + 1]),
            (coefs[i + 1] * (v - letters[i]) + ys[i]),
            new,
        )
    return np.uint8(new)


def main():
    # EXAMPLE ON PRESENTATION
    params = [[50, 150], [0.2, 2, 1], [30, 200]]

    params2 = [[40, 90, 140], [0.2, 3, 1.8, 2], [40, 90, 180]]

    img = cv2.imread("woman.jpg")
    stretched_contrast = stretch_contrast(img, params)
    stretched_contrast2 = stretch_contrast(img, params2)
    cv2.imshow("woman", stretched_contrast)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("woman", stretched_contrast2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("woman_stretched.jpg", stretched_contrast)
    cv2.imwrite("woman_stretched2.jpg", stretched_contrast2)


main()
