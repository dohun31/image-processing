"""
영상비전처리 과제 #2
201911900 백도훈 
5-6 주파수 공간에서의 필터링
"""
import cv2 
import numpy as np
from matplotlib import pyplot as plt

def show_image():
    plt.subplot(171),plt.imshow(in_img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(172),plt.imshow(dft_img, cmap = 'gray')
    plt.title('DFT'), plt.xticks([]), plt.yticks([])
    plt.subplot(173),plt.imshow(shift1_img, cmap = 'gray')
    plt.title('Shift'), plt.xticks([]), plt.yticks([])
    plt.subplot(174),plt.imshow(LPF, cmap = 'gray')
    plt.title('LPF'), plt.xticks([]), plt.yticks([])
    plt.subplot(175),plt.imshow(mul_img, cmap = 'gray')
    plt.title('Multiply'), plt.xticks([]), plt.yticks([])
    plt.subplot(176),plt.imshow(shift2_img, cmap = 'gray')
    plt.title('Shift2'), plt.xticks([]), plt.yticks([])
    plt.subplot(177),plt.imshow(cv2.blur(in_img, ksize=(5, 5)), cmap = 'gray')
    plt.title('Result'), plt.xticks([]), plt.yticks([])
    plt.show()

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

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
    return np.log(np.abs(out_img))

def get_LPF(c):
    import math
    LPF = np.zeros((row, col), np.uint8)
    rrow, ccol = int(row / 2), int(col / 2)
    for i in range(row):
        for j in range(col):
            d = math.sqrt((j - ccol) ** 2 + (i - rrow) ** 2)
            if d <= c:
                LPF[i][j] = 1
            else:
                LPF[i][j] = 0
    return LPF

def idft(dft_shift):
    dft_ishift = np.fft.ifftshift(dft_shift) 
    out_img = cv2.idft(dft_ishift) 
    out_img = cv2.magnitude(out_img[:, :], out_img[:, :])
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    dft_img = dft()
    shift1_img = np.fft.fftshift(dft_img)
    LPF = get_LPF(80)
    mul_img = np.multiply(shift1_img, LPF)
    shift2_img = np.fft.fftshift(mul_img)
    out_img = cv2.idft(shift1_img)
    show_image()
