"""
영상비전처리 과제 #1 
201911900 백도훈 
2. 반전 영상
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif", cv2.IMREAD_GRAYSCALE)
    low, high = in_img.min(), in_img.max()
    row, col = in_img.shape
    return in_img, low, high, row, col

def show_result_image(out_img):
    title = 'reversed'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

def reversed_image():
    out_img = copy.deepcopy(in_img)
    for i in range(row):
        for j in range(col):
            # 255에서 원래 값을 빼줌 -> 반전 시키기
            old_pixel = out_img[i][j]
            new_pixel = 255 - old_pixel
            out_img[i][j] = new_pixel
    return out_img

if __name__ == "__main__":
    in_img, low, high, row, col = image_handler()
    out_img = reversed_image()
    show_result_image(out_img)