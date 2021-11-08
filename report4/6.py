"""
영상비전처리 과제 #2
201911900 백도훈 
4-6. alpha trimmed mean 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'alpha-trimmed'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def find_avg(values):
    sumv = sum(values)
    return int(sumv / len(values))

def find_value(ni, nj):
    values = []
    for ci in range(ni - 1, ni + 2):
        for cj in range(nj - 1, nj + 2):
            if 0 <= ci < row and 0 <= cj < col:
                values.append(in_img[ci][cj])
            else:
                values.append(0)
    return find_avg(values[2:7]) # alpha == 0.3

def alpha_trimmed_filter():
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            out_img[i][j] = find_value(i, j)
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = alpha_trimmed_filter()
    show_result_image(out_img)