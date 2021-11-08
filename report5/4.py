"""
영상비전처리 과제 #2
201911900 백도훈 
5- 주파수 영역에서의 LPF 프로그램
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_image():
    plt.subplot(131),plt.imshow(in_img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(out, cmap = 'gray')
    plt.title(''), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(LPF, cmap = 'gray')
    plt.title('LPF'), plt.xticks([]), plt.yticks([])
    plt.show()

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def filtering():
    dft = cv2.dft(np.float32(in_img), flags=cv2.DFT_COMPLEX_OUTPUT) 
    dft_shift = np.fft.fftshift(dft)
    LPF = np.zeros((row, col, 2), np.uint8)
    rrow, ccol = int(row / 2), int(col / 2)
    LPF[rrow - 50:rrow + 50, ccol - 50:ccol + 50] = 1
    LPF_shift = dft_shift * LPF 
    LPF_ishift = np.fft.ifftshift(LPF_shift) 
    LPF_img = cv2.idft(LPF_ishift) 
    LPF_img = cv2.magnitude(LPF_img[:, :, 0], LPF_img[:, :, 1]) 
    out = 20*np.log(cv2.magnitude(LPF_shift[:, :, 0], LPF_shift[:, :, 1]))
    return LPF_img, out

if __name__ == "__main__":
    in_img, row, col = image_handler()
    LPF, out = filtering()
    show_image()