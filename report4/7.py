"""
영상비전처리 과제 #2
201911900 백도훈 
4-7. 캐니 프로그램
"""
import cv2
import copy
import math
import numpy as np

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'canny'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_mask_processing(i, j, mask, in_img):
    sumv = 0
    if len(mask) == 3:
        dpoint = [-1, 0, 1]
    else:
        dpoint = [-2, -1, 0, 1, 2]
    for i_idx, di in enumerate(dpoint):
        for j_idx, dj in enumerate(dpoint):
            ni = i + di
            nj = j + dj
            if 0 <= ni < row and 0 <= nj < col:
                sumv += in_img[ni][nj] * mask[i_idx][j_idx]
    if sumv < 0: sumv = 0
    elif sumv > 255: sumv = 255
    return sumv

def gaussian_image():
    mask = [
        [2/159, 4/159, 5/159, 4/159, 2/159],
        [4/159, 9/159, 12/159, 9/159, 4/159],
        [5/159, 12/159, 15/159, 12/159, 5/159],
        [4/159, 9/159, 12/159, 9/159, 4/159],
        [2/159, 4/159, 5/159, 4/159, 2/159],
    ]
    out_img = copy.deepcopy(in_img)
    # 마스크 프로세싱
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_mask_processing(i, j, mask, in_img)
    return out_img

def add(h, v):
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            out_img[i][j] = int(h[i][j]) + int(v[i][j])
    return out_img

def nonmax_suppression(sobel, direct):
    rows, cols = sobel.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # 관심 영역 참조 통해 이웃 화소 가져오기
            values = sobel[i-1:i+2, j-1:j+2].flatten()
            first = [3, 0, 1, 2]
            id = first[direct[i, j]]
            v1, v2 = values[id], values[8-id]
            dst[i, j] = sobel[i, j] if (v1 < sobel[i, j] > v2) else 0
    return dst

def trace(max_sobel, i, j, low):
    h, w = max_sobel.shape
    if (0 <= i < h and 0 <= j < w) == False: return
    if pos_ck[i, j] > 0 and max_sobel[i, j] > low:
        pos_ck[i, j] = 255
        canny[i, j] = 255
        trace(max_sobel, i-1, j-1, low)
        trace(max_sobel, i, j-1, low)
        trace(max_sobel, i+1, j-1, low)
        trace(max_sobel, i-1, j, low)
        trace(max_sobel, i+1, j, low)
        trace(max_sobel, i-1, j+1, low)
        trace(max_sobel, i, j+1, low)
        trace(max_sobel, i+1, j+1, low)

def hysteresis_th(max_sobel, low, high):
    rows, cols = max_sobel.shape[:2]
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if max_sobel[i, j] >= high: trace(max_sobel, i, j, low)

# def sobel_filtering(in_img):
#     horizon_out_img = copy.deepcopy(in_img)
#     vertical_out_img = copy.deepcopy(in_img)
#     SOBEL_MASK = [[[-1, -2, -1], [0, 0, 0], [1, 2, 1]], [[1, 0, -1], [2, 0, -2], [1, 0, -1]]]
#     magnitude = [[0 for _ in range(col)] for _ in range(row)]
#     phase = [[0 for _ in range(col)] for _ in range(row)]
#     for i in range(row):
#         for j in range(col):
#             h = on_mask_processing(i, j, SOBEL_MASK[0], in_img)
#             v = on_mask_processing(i, j, SOBEL_MASK[1], in_img)
#             horizon_out_img[i][j] = h
#             vertical_out_img[i][j] = v
#             magnitude[i][j] = math.sqrt(h ** 2 + v ** 2)
#             phase[i][j] = math.atan(abs(h) / abs(v)) if v != 0 else 0
#             minv = 180
#             minidx = 0
#             for idx, degree in enumerate([0, 45, 90, 135]):
#                 v = abs(phase[i][j] - degree)
#                 if v < minv:
#                     minv = v
#                     minidx = idx
#             phase[i][j] = [0, 45, 90, 135][minidx]
#     out_img = add(horizon_out_img, vertical_out_img)
#     return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    pos_ck = np.zeros(in_img.shape[:2], np.uint8)
    canny = np.zeros(in_img.shape[:2], np.uint8)
    gaussian_img = gaussian_image()
    Gx = cv2.Sobel(np.float32(gaussian_img), cv2.CV_32F, 1, 0, 3)
    Gy = cv2.Sobel(np.float32(gaussian_img), cv2.CV_32F, 0, 1, 3)
    sobel = cv2.magnitude(Gx, Gy)
    sobel = np.clip(sobel, 0, 255).astype(np.uint8)
    directs = cv2.phase(Gx, Gy) / (np.pi/4)
    directs = directs.astype(int) % 4
    max_sobel = nonmax_suppression(sobel, directs)
    max_sobel = max_sobel.astype(np.uint8)
    checker = sobel >= max_sobel
    unique, counts = np.unique(checker, return_counts=True)
    checker = dict(zip(unique, counts))
    nonmax = max_sobel.copy()
    hysteresis_th(max_sobel, 100, 150)
    canny = max_sobel.copy()
    show_result_image(canny)
    canny2 = cv2.Canny(in_img, 100, 150)
    show_result_image(canny2)