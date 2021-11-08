"""
영상비전처리 과제 #2
201911900 백도훈 
4-3. 미디언 필터 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'median'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def find_median(ni, nj):
    values = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ci = ni + di
            cj = nj + dj
            if 0 <= ci < row and 0 <= cj < col:
                values.append(in_img[ci][cj])
            else:
                values.append(0)
    return sorted(values)[4]

def median_filter():
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            out_img[i][j] = find_median(i, j)
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = median_filter()
    show_result_image(out_img)