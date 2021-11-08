"""
영상비전처리 과제 #2
201911900 백도훈 
4-2. nagao-matsuyama 연산자 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'kuwahara'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def find_mean(point, ni, nj):
    sumv = 0
    point.append((0, 0))
    for di, dj in point:
        ci = ni + di
        cj = nj + dj
        if 0 <= ci < row and 0 <= cj < col:
            sumv += in_img[ci][cj]
    return sumv / 7

def find_var(point, mean, ni, nj):
    sumv = 0
    point.append((0, 0))
    for di, dj in point:
        ci = ni + di
        cj = nj + dj
        if 0 <= ci < row and 0 <= cj < col:
            sumv += (in_img[ci][cj] - mean) ** 2
    return sumv / 7

def kuwahara():
    out_img = copy.deepcopy(in_img)
    points = [[(-2, -1), (-2, 0), (-2, 1), (-1, -1), (-1, 0), (-1, 1)],
            [(-1, 1), (-1, 2), (0, 1), (0, 2), (1, 1), (1, 2)],
            [(2, -1), (2, 0), (2, 1), (1, -1), (1, 0), (1, 2)],
            [(-1, -2), (-1, -1), (0, -2), (0, -1), (1, -2), (1, -1)],
            [(-2, -2), (-2, -1), (-1, -2), (-1, -1), (-1, 0), (0, -1)],
            [(-2, 1), (-2, 2), (1, 0), (1, 1), (1, 2), (0, 1)],
            [(0, 1), (-1, 0), (-1, 1), (-1, 2), (-2, 1), (-2, 2)],
            [(0, -1), (1, -2), (1, -1), (1, 0), (2, -2), (2, -1)]]
    for i in range(row):
        for j in range(col):
            # 평균 구하기
            means = [find_mean(points[idx], i, j) for idx in range(8)]
            # 분산 구하기
            vars = [find_var(points[idx], means[idx], i, j) for idx in range(8)]
            # 최소 분산 구하기
            minv = vars.index(min(vars))
            out_img[i][j] = means[minv]
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = kuwahara()
    show_result_image(out_img)