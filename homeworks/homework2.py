import cv2
import numpy as np
import matplotlib.pyplot as plt


def compass(i_m=-1, o_p=1):
    # Generiranje na potrebnite 3x3 filter matrici za compass filterot
    cmp = []
    tl = np.matrix([[o_p, o_p, 0], [o_p, 0, i_m], [0, i_m, i_m]])
    cmp.append(tl)
    ll = np.matrix([[1, 0, -1]] * 3)
    cmp.append(ll)
    bl = np.flip(tl, axis=0)
    cmp.append(bl)
    tt = np.rot90(ll, axes=(1, 0))
    cmp.append(tt)
    tr = np.flip(tl, axis=1)
    cmp.append(tr)
    rr = np.flip(ll, axis=1)
    cmp.append(rr)
    rb = np.flip(tr, axis=0)
    cmp.append(rb)
    bb = np.flip(tt, axis=0)
    cmp.append(bb)
    return cmp


def task1(gray_img):
    cmp_filter = compass()
    FILTER_LIST = [cv2.filter2D(gray_img, -1, fill) for fill in cmp_filter]

    f, axarr = plt.subplots(4, 2, figsize=(30, 30))
    plt.suptitle("ALL THE FILTERS FROM COMPASS EDGE DETECTOR")
    plt.subplots_adjust(wspace=0.2, hspace=0.3, right=0.4, left=0)
    for i in range(2):
        for j in range(4):
            axarr[j, i].imshow(
                cv2.cvtColor(FILTER_LIST[(i * 4) + j], cv2.COLOR_BGR2RGB)
            )
            title = [i.tolist() for i in compass()]
            axarr[j, i].set_title(f"{title[i*4+j]}")
    plt.savefig("8_separete_filters.png", bbox_inches="tight")
    plt.show()


def task2_1(gray_img):
    FILTER_LIST = [cv2.filter2D(gray_img, -1, fill) for fill in compass()]
    FINAL = np.max([c for c in FILTER_LIST], axis=0)
    cv2.imwrite("final_result.png", FINAL)
    cv2.imshow("Final result", FINAL)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def task2_2(gray_img):
    RES = []
    for x in range(1, 7):
        FILTER_LIST = [cv2.filter2D(gray_img, -1, fill) for fill in compass(-x, x)]
        RES.append(np.max([c for c in FILTER_LIST], axis=0))

    f, axarr = plt.subplots(3, 2, figsize=(30, 30))
    plt.suptitle("COMPASS EDGE RESULTS FOR DIFERENT THRESHOLDS")
    plt.subplots_adjust(wspace=0.2, hspace=0.3, right=0.4, left=0)
    for i in range(2):
        for j in range(3):
            axarr[j, i].imshow(cv2.cvtColor(RES[i*3 + j], cv2.COLOR_BGR2RGB))
            axarr[j, i].set_title(f"COMPASS FILTER VALUES: {i*3+j}")
    plt.savefig("6_praga.png", bbox_inches="tight")
    plt.show()


def main():
    MAIN_IMG = cv2.imread("Lenna.png", 0)
    task1(MAIN_IMG)
    task2_1(MAIN_IMG)
    task2_2(MAIN_IMG)


main()
