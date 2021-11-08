"""
영상비전처리 과제 #2
201911900 백도훈 
4-5. 최대/최소값 필터 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(title, out_img):
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def find_value(ni, nj, state):
    values = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ci = ni + di
            cj = nj + dj
            if 0 <= ci < row and 0 <= cj < col:
                values.append(in_img[ci][cj])
    if state == "MAX": return max(values)
    elif state == "MIN": return min(values)

def filter(state):
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            out_img[i][j] = find_value(i, j, state)
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    minimum_img = filter("MIN")
    maximum_img = filter("MAX")
    cv2.imshow('ORIGIN', in_img)
    cv2.imshow('MIN', minimum_img)
    cv2.imshow('MAX', maximum_img)
    cv2.waitKey(0)