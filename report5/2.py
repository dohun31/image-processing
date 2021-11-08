"""
영상비전처리 과제 #2
201911900 백도훈 
5-2 2D FFT를 이용한 주파수 변환 및 역변환
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
    plt.subplot(132),plt.imshow(fft_out_img, cmap = 'gray')
    plt.title('FFT'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(ifft_out_img, cmap = 'gray')
    plt.title('IFFT'), plt.xticks([]), plt.yticks([])
    plt.show()

def fft():
    out_img = np.fft.fft2(in_img)
    fshift = np.fft.fftshift(out_img)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    return fshift, magnitude_spectrum

def ifft():
    crow,ccol = round(row / 2), round(col / 2)
    fshift[crow-30:crow+60, ccol-30:ccol+30] = 0 
    f_ishift = np.fft.ifftshift(fshift) 
    img_back = np.fft.ifft2(f_ishift) 
    img_back = np.abs(img_back)
    return img_back

if __name__ == "__main__":
    in_img, row, col = image_handler()
    fshift, fft_out_img = fft()
    ifft_out_img = ifft()
    show_image()