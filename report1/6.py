"""
영상비전처리 과제 #1 
201911900 백도훈 
6. 히스토그램 명세화
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    low, high = in_img.min(), in_img.max()
    row, col = in_img.shape
    return in_img, low, high, row, col

def show_result_image(out_img):
    title = 'specification'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

def get_histogram(img):
    histogram = [0] * 256 # histogram 초기화
    for i in range(row):
        for j in range(col):
            histogram[img[i][j]] += 1 # histogram 구하기
    return histogram

def get_prefix_sum(histogram):
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
        normalization[i] = data
    return normalization

def get_renormalization(normalization):
    renormalization = [0] * 256
    for i in range(256):
        minv = 256
        nowv = i
        for j in range(256):
            curv = normalization[j]
            if minv > abs(nowv - curv):
                minv = abs(nowv - curv)
                target_idx = j
        renormalization[i] = target_idx
    return renormalization

# 히스토그램 평활화 프로그램
def histogram_specification():
    out_img = copy.deepcopy(in_img)
    # 누적합 구하기
    target_prefix_sum = get_prefix_sum(target_histogram)
    # 정규화
    target_normalization = get_normalization(target_prefix_sum)
    # 타겟의 역평활화 값
    renormalization = get_renormalization(target_normalization)
    # 새로운 명도 값으로 변경
    for i in range(row):
        for j in range(col):
            old_pixel = out_img[i][j]
            new_pixel = renormalization[old_pixel]
            out_img[i][j] = new_pixel
    return out_img

if __name__ == "__main__":
    in_img, low, high, row, col = image_handler()

    target_img_src = "/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/spe.jpeg";
    target_histogram = get_histogram(cv2.imread(target_img_src, cv2.IMREAD_GRAYSCALE))

    out_img = histogram_specification()
    show_result_image(out_img)