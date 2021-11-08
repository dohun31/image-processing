"""
영상비전처리 과제 #2
201911900 백도훈 
5-3 셔플링
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_image():
    plt.subplot(131),plt.imshow(in_img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(out_img, cmap = 'gray')
    plt.title('before'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(shuffle_img, cmap = 'gray')
    plt.title('Shuffle'), plt.xticks([]), plt.yticks([])
    plt.show()

def dft():
    t = np.zeros((row ,col),complex)
    out_img = np.zeros((row, col),complex)
    m = np.arange(row)
    n = np.arange(col)
    x = m.reshape((row,1))
    y = n.reshape((col,1))
    for r in range(0, row):
        M1 = 1j*np.sin(-2*np.pi*y*n/col) + np.cos(-2*np.pi*y*n/col)
        t[r] = np.dot(M1, in_img[r])
    for c in range(0, col):
        M2 = 1j*np.sin(-2*np.pi*x*m/col) + np.cos(-2*np.pi*x*m/col)
        out_img[:,c] = np.dot(M2, t[:,c])
    return  np.log(np.abs(out_img))

def shuffleDFT(in_img):
    out_img = np.copy(in_img)
    shuffle_img = np.copy(in_img)
    rrow, ccol = round(row / 2), round(col / 2)
    a1, a2 = out_img[0:rrow, 0:ccol], out_img[rrow:row, ccol:col]
    b1, b2 = out_img[0:rrow, ccol:col], out_img[rrow:row, 0:ccol]
    shuffle_img[0:rrow, 0:ccol] = a2
    shuffle_img[rrow:row, ccol:col] = a1
    shuffle_img[0:rrow, ccol:col] = b2
    shuffle_img[rrow:row, 0:ccol] = b1
    return shuffle_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = dft()
    shuffle_img = shuffleDFT(out_img)
    show_image()