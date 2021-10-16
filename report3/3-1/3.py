"""
영상비전처리 과제 #2
201911900 백도훈 
3-1-3. 로버츠, 프리윗, 소벨 연산자 프로그램
"""
import cv2
import copy
import numpy as np
import matplotlib as plt

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def on_mask_processing(mask, arr):
    sumv = np.sum(np.multiply(mask, arr))
    if sumv < 0: sumv = 0
    elif sumv > 255: sumv = 255
    return sumv

def filtering(MASK, name):
    horizon_out_img = copy.deepcopy(in_img)
    vertical_out_img = copy.deepcopy(in_img)
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            arr = in_img[i - 1:i + 2, j - 1:j + 2]
            horizon_out_img[i][j] =  on_mask_processing(MASK[0], arr)
            vertical_out_img[i][j] = on_mask_processing(MASK[1], arr)
    cv2.imwrite(f'{name}.png', np.add(horizon_out_img, vertical_out_img))
    

if __name__ == "__main__":
    ROBERTS_MASK = [[[-1, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, -1], [0, 1, 0], [0, 0, 0]]]
    PREWITT_MASK = [[[-1, -1, -1], [0, 0, 0], [1, 1, 1]], [[1, 0, -1], [1, 0, -1], [1, 0, -1]]]
    SOBEL_MASK = [[[-1, -2, -1], [0, 0, 0], [1, 2, 1]], [[1, 0, -1], [2, 0, -2], [1, 0, -1]]]
    in_img, row, col = image_handler()
    roberts_out_img =  filtering(ROBERTS_MASK, 'roberts')
    prewitt_out_img = filtering(PREWITT_MASK, 'prewitt')
    sobel_out_img = filtering(SOBEL_MASK, 'sobel')