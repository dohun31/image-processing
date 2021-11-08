"""
영상비전처리 과제 #2
201911900 백도훈 
4-1. kuwahara 연산자 프로그램
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

def find_mean(point):
    sumv = 0
    ni, nj = point
    for i in range(ni, ni + 3):
        for j in range(nj, nj + 3):
            if 0 <= i < row and 0 <= j < col:
                sumv += in_img[i][j]
    return sumv / 9

def find_var(point, mean):
    sumv = 0
    ni, nj = point
    for i in range(ni, ni + 3):
        for j in range(nj, nj + 3):
            if 0 <= i < row and 0 <= j < col:
                sumv += (in_img[i][j] - mean) ** 2
    return sumv / 9

def kuwahara():
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            # 사분면
            points = [(i - 2, j - 2), (i - 2, j), (i, j - 2), (i, j)]
            # 평균 구하기
            means = [find_mean(points[idx]) for idx in range(4)]
            # 분산 구하기
            vars = [find_var(points[idx], means[idx]) for idx in range(4)]
            # 최소 분산 구하기
            minv = vars.index(min(vars))
            out_img[i][j] = means[minv]
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = kuwahara()
    show_result_image(out_img)