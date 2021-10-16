"""
영상비전처리 과제 #2
201911900 백도훈 
2-3. 가우시안 스무딩 필터링 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    row, col = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'gaussian'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def on_mask_processing(i, j):
    # 마스크 계산 값을 저장할 변수 s를 0으로 초기화
    s = 0
    for m in mask:
        for (di, dj), v in m:
            ci = i + di
            cj = j + dj
            if 0 <= ci < row and 0 <= cj < col:
                s += in_img[ci][cj] * v
    # overflow 방지
    if s > 255: s = 255
    elif s < 0: s = 0
    return s

def gaussian_image():
    out_img = copy.deepcopy(in_img)
    # 마스크 프로세싱
    for i in range(row):
        for j in range(col):
            out_img[i][j] = on_mask_processing(i, j)
    return out_img

if __name__ == "__main__":
    mask = [
        [[(-2, -2), 1/273],[(-2, -1), 4/273], [(-2, 0), 7/273], [(-2, 1), 4/273/273], [(-2, 2), 1/273]],
        [[(-1, -2), 4/273],[(-1, -1), 16/273], [(-1, 0), 26/273], [(-1, 1), 16/273], [(-1, 2), 4/273]],
        [[(0, -2), 7/273],[(0, -1), 26/273], [(0, 0), 41/273], [(0, 1), 26/273], [(0, 2), 7/273]],
        [[(1, -2), 4/273],[(1, -1), 16/273], [(1, 0), 26/273], [(1, 1), 16/273], [(1, 2), 4/273]],
        [[(2, -2), 1/273],[(2, -1), 4/273], [(2, 0), 7/273], [(2, 1), 4/273], [(2, 2), 1/273]],
    ]
    in_img, row, col = image_handler()
    out_img = gaussian_image()
    show_result_image(out_img)