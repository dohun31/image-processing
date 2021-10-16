"""
영상비전처리 과제 #2
201911900 백도훈 
3-1-4. 라플라시안 연산자 프로그램
"""
import cv2
import copy
import numpy as np

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/sudoku.jpeg", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'laplacian'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_mask_processing(arr):
    sumv = np.sum(np.multiply(laplacian_mask, arr))
    if sumv < 0: sumv = 0
    elif sumv > 255: sumv = 255
    return sumv

def laplacian_operator():
    out_img = copy.deepcopy(in_img)
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            out_img[i][j] = on_mask_processing(in_img[i - 1:i + 2, j - 1:j + 2])
    return out_img

if __name__ == "__main__":
    laplacian_mask = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
    in_img, row, col = image_handler()
    out_img= laplacian_operator()
    show_result_image(out_img)