"""
영상비전처리 과제 #1 
201911900 백도훈 
3. 기본 명암 대비 스트레칭
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    low, high = in_img.min(), in_img.max()
    row, col = in_img.shape
    return in_img, low, high, row, col

def show_result_image(out_img):
    title = 'stretching'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

# 기본 명암 대비 스트레칭 기법 프로그램
def stretching():
    out_img = copy.deepcopy(in_img)
    # low는 최저 명도, high는 최대 명도
    for i in range(row):
        for j in range(col):
            old_pixel = out_img[i][j] # 현재 명도
            new_pixel = ((old_pixel - low) / (high - low))  * 255  # 스트레치 후 명도
            out_img[i][j] = new_pixel 
    return out_img

if __name__ == "__main__":
    in_img, low, high, row, col = image_handler()
    out_img = stretching()
    show_result_image(out_img)