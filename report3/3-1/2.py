"""
영상비전처리 과제 #2
201911900 백도훈 
3-1-2. 차 연산자 기법 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'difference_operator'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_mask_processing(i, j):
    maxv = 0
    points = [[(-1, -1), (1, 1)], [(-1, 0), (1, 0)], [(1, -1), (-1, 1)], [(0, 1), (1, 0)]]
    for point in points:
        pv = []
        for di, dj in point:
            ni = i + di
            nj = j + dj
            pv.append(int(in_img[ni][nj]) if 0 <= ni < row and 0 <= nj < col else 0)
        maxv = max(maxv, abs(pv[0] - pv[1]))
    return maxv

def difference_operator():
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_mask_processing(i, j)
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img= difference_operator()
    show_result_image(out_img)