"""
영상비전처리 과제 #2
201911900 백도훈 
2-7. 가우시안 잡음 -> LPF
"""
import cv2
import copy
import numpy as np

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'LPF-gaussian'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_noise_preocessing(i, j, std):
    noise = np.random.normal()
    result_noise = in_img[i][j] +  std * noise
    return result_noise

def on_mask_processing(i, j, mask, in_img):
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

def get_gaussian_image(in_img):
    out_img = copy.deepcopy(in_img)
    # 마스크 프로세싱
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_noise_preocessing(i, j, 20)
    return out_img

def get_lpf_image(in_img, mask):
    out_img = copy.deepcopy(in_img)
    # 마스크 프로세싱
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_mask_processing(i, j, mask, in_img)
    return out_img

if __name__ == "__main__":
    lpf_mask = [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]
    in_img, row, col = image_handler()
    # 가우시안 잡음 적용
    gaussian_img = get_gaussian_image(in_img)
    show_result_image(gaussian_img)
    # LPF 적용
    out_img = get_lpf_image(gaussian_img, lpf_mask)
    show_result_image(out_img)