"""
영상비전처리 과제 #1 
201911900 백도훈 
5. 히스토그램 평활화
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    low, high = in_img.min(), in_img.max()
    row, col = in_img.shape

    histogram = [0] * 256 # histogram 초기화
    for i in range(row):
        for j in range(col):
            histogram[in_img[i][j]] += 1 # histogram 구하기

    return in_img, low, high, row, col, histogram

def show_result_image(out_img):
    title = 'equalization'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

def get_prefix_sum():
    # 누적합 구하기
    prefix_sum = [0] * 256
    prefix_sum[0] = histogram[0]
    for i in range(1, 256):
        prefix_sum[i] = prefix_sum[i - 1] + histogram[i]
    return prefix_sum

def get_normalization(prefix_sum):
    normalization = [0] * 256
    N = row * col # 화소의 총 개수
    for i in range(256):
        data =  prefix_sum[i] * high / N
        normalization[i] = round(data)
    return normalization

# 히스토그램 평활화 프로그램
def histogram_equalizaion():
    out_img = copy.deepcopy(in_img)
    # 누적합 구하기
    prefix_sum = get_prefix_sum()
    # 정규화
    normalization = get_normalization(prefix_sum)
    # 새로운 명도 값으로 변경
    for i in range(row):
        for j in range(col):
            old_pixel = out_img[i][j]
            new_pixel = normalization[old_pixel]
            out_img[i][j] = new_pixel
    return out_img

if __name__ == "__main__":
    in_img, low, high, row, col, histogram = image_handler()
    out_img = histogram_equalizaion()
    show_result_image(out_img)