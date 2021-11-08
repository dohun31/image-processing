"""
영상비전처리 과제 #2
201911900 백도훈 
4-3. 하이브리드 미디언 필터 프로그램
"""
import cv2
import copy
import numpy as np

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'hybrid-median'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_noise_preocessing(i, j, std):
    noise = np.random.normal()
    result_noise = in_img[i][j] +  std * noise
    return result_noise

def noise_filter():
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_noise_preocessing(i, j, 20)
    return out_img

def find_median(ni, nj):
    values = [in_img[ni][nj]]
    # 대각선 돌기
    for diagonal in diagonals:
        nowv = []
        for di, dj in diagonal:
            ci = ni + di
            cj = nj + dj
            if 0 <= ci < row and 0 <= cj < col:
                nowv.append(in_img[ci][cj])
            else:
                nowv.append(0)
        # 대각선의 중간값 values에 push
        values.append(sorted(nowv)[2])
    # 최종 중간값 return
    return sorted(values)[1]

def hybrid_median_filter(in_img):
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            out_img[i][j] = find_median(i, j)
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    diagonals = [[(-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2)],
                [(2, 2), (1, 1), (0, 0), (-1, -1), (-2, -2)]]
    noise_img = noise_filter()
    out_img = hybrid_median_filter(noise_img)
    cv2.imshow('original', in_img)
    cv2.imshow('noise',noise_img)
    cv2.imshow('hybrid',out_img)
    cv2.waitKey(0)