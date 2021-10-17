"""
영상비전처리 과제 #2
201911900 백도훈 
3-2-2. RGB - HSI 변환 프로그램
"""
import cv2
import numpy as np
from math import acos, pi, radians, sqrt

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif")
    row, col, _ = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'RGB-to-HSI'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def get_intensity(R, G, B):
    I = np.divide(R + G + B, 3)
    return I

def get_saturation(R, G, B):
    minv = np.minimum(R, np.minimum(G, B))
    sumv = R + G + B + 0.0001
    S = 1 - 3 / (sumv) * minv
    return S

def get_hue(R, G, B):
    H = np.copy(R) # 한 층 복사
    for i in range(row):
        for j in range(col):
            value = 0.5 * ((R[i][j] - G[i][j]) + (R[i][j] - B[i][j])) / sqrt((R[i][j] - G[i][j]) ** 2 + ((R[i][j] - B[i][j]) * (G[i][j] - B[i][j])))
            theta = acos(value)
            if G[i][j] >= B[i][j]: hue = theta
            else: hue = 360 * pi / 180.0 - theta
            H[i][j] = hue
    return H

def convert_to_HSI():
    tmp_img = np.float32(in_img) / 255
    R, G, B = tmp_img[:, :, 2], tmp_img[:, :, 1], tmp_img[:, :, 0]
    I = get_intensity(R, G, B)
    S = get_saturation(R, G, B)
    H = get_hue(R, G, B)
    show_result_image(I)
    show_result_image(S)
    show_result_image(H)
    return cv2.merge((H, S, I))

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = convert_to_HSI()
    show_result_image(out_img)