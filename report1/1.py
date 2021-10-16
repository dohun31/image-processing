"""
영상비전처리 과제 #1 
201911900 백도훈 
1. 이진 영상
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    low, high = in_img.min(), in_img.max()
    row, col = in_img.shape
    return in_img, low, high, row, col

def show_result_image(out_img):
    title = 'binary'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def binary_image():
    out_img = copy.deepcopy(in_img)
    # 임계값 임의로 설정 최대 명도와 최대 명도의 중간
    threshold = int((high - low) / 2)
    # pixel 전체 돌면서 이진화(binary) 해주기
    for i in range(row):
        for j in range(col):
            # 임계값보다 작으면 0 크거나 같으면 255
            old_pixel = out_img[i][j]
            new_pixel = 0 if old_pixel < threshold else 255
            out_img[i][j] = new_pixel
    return out_img

if __name__ == "__main__":
    in_img, low, high, row, col = image_handler()
    out_img = binary_image()
    show_result_image(out_img)