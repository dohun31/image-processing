"""
영상비전처리 과제 #2
201911900 백도훈 
5-5 주파수 영역에서의 HPF 프로그램  
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_image():
    plt.subplot(131),plt.imshow(in_img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(out, cmap = 'gray')
    plt.title('out'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(HPF, cmap = 'gray')
    plt.title('HPF'), plt.xticks([]), plt.yticks([])
    plt.show()

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def filtering():
    dft = cv2.dft(np.float32(in_img), flags=cv2.DFT_COMPLEX_OUTPUT) 
    dft_shift = np.fft.fftshift(dft)
    HPF = np.ones((row, col, 2), np.uint8)
    rrow, ccol = int(row / 2), int(col / 2)
    HPF[rrow - 50:rrow + 50, ccol - 50:ccol + 50] = 0
    HPF_shift = dft_shift * HPF 
    HPF_ishift = np.fft.ifftshift(HPF_shift) 
    HPF_img = cv2.idft(HPF_ishift) 
    HPF_img = cv2.magnitude(HPF_img[:, :, 0], HPF_img[:, :, 1]) 
    out = 20*np.log(cv2.magnitude(HPF_shift[:, :, 0], HPF_shift[:, :, 1]))
    return HPF_img, out

if __name__ == "__main__":
    in_img, row, col = image_handler()
    HPF, out = filtering()
    show_image()