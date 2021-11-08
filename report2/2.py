"""
영상비전처리 과제 #2
201911900 백도훈 
2-2. 블러링 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'blurring'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_mask_processing(i, j):
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

def blurring_image():
    out_img = copy.deepcopy(in_img)
    # 마스크 프로세싱
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_mask_processing(i, j)
    return out_img

if __name__ == "__main__":
    mask = [[1/9 for _ in range(3)] for _ in range(3)]
    in_img, row, col = image_handler()
    out_img = blurring_image()
    show_result_image(out_img)
