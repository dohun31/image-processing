"""
영상비전처리 과제 #2
201911900 백도훈 
5-1 2D DFT를 이용한 2차원 주파수 변환 및 역변환
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
    plt.title('DFT'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(in_img, cmap = 'gray')
    plt.title('IDFT'), plt.xticks([]), plt.yticks([])
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
    return np.log(np.abs(out_img))

def idft():
    fshift = np.copy(out_img)
    crow,ccol = round(row / 2), round(col / 2)
    fshift[crow-30:crow+60, ccol-30:ccol+30] = 0 
    f_ishift = np.fft.ifftshift(fshift) 
    img_back = np.fft.ifft2(f_ishift) 
    img_back = np.abs(img_back)
    return img_back

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = dft()
    idft_out_img = idft()
    show_image()