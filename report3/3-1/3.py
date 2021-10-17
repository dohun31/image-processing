"""
영상비전처리 과제 #2
201911900 백도훈 
3-1-3. 로버츠, 프리윗, 소벨 연산자 프로그램
"""
import cv2
import copy
import numpy as np

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(title, out_img):
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_mask_processing(i, j, mask):
    sumv = 0
    for i_idx, di in enumerate([-1, 0, 1]):
        for j_idx, dj in enumerate([-1, 0, 1]):
            ni = i + di
            nj = j + dj
            if 0 <= ni < row and 0 <= nj < col:
                sumv += in_img[ni][nj] * mask[i_idx][j_idx]
    if sumv < 0: sumv = 0
    elif sumv > 255: sumv = 255
    return sumv

def filtering(MASK, name):
    horizon_out_img = copy.deepcopy(in_img)
    vertical_out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            horizon_out_img[i][j] =  on_mask_processing(i, j, MASK[0])
            vertical_out_img[i][j] = on_mask_processing(i, j, MASK[1])
    show_result_image(f'{name}-horizon.png', horizon_out_img) # 수평
    show_result_image(f'{name}-vertical.png', vertical_out_img) # 수직
    show_result_image(f'{name}.png', np.add(horizon_out_img, vertical_out_img)) # 결과

if __name__ == "__main__":
    ROBERTS_MASK = [[[-1, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, -1], [0, 1, 0], [0, 0, 0]]]
    PREWITT_MASK = [[[-1, -1, -1], [0, 0, 0], [1, 1, 1]], [[1, 0, -1], [1, 0, -1], [1, 0, -1]]]
    SOBEL_MASK = [[[-1, -2, -1], [0, 0, 0], [1, 2, 1]], [[1, 0, -1], [2, 0, -2], [1, 0, -1]]]
    in_img, row, col = image_handler()
    filtering(ROBERTS_MASK, 'roberts') # 로버츠
    filtering(PREWITT_MASK, 'prewitt') # 프리윗
    filtering(SOBEL_MASK, 'sobel') # 소벨