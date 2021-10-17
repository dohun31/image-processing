"""
영상비전처리 과제 #2
201911900 백도훈 
3-2-1. RGB - CMY 변환 프로그램
"""
import cv2
import copy

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif")
    row, col, _ = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'RGB-to-CMY'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def convert_to_CMY():
    out_img = copy.deepcopy(in_img)
    R, G, B = in_img[:, :, 2], in_img[:, :, 1], in_img[:, :, 0]
    for i in range(row):
        for j in range(col):
            C = 255 - R[i][j]
            M = 255 - G[i][j]
            Y = 255 - B[i][j]
            out_img[i][j][0] = Y
            out_img[i][j][1] = M
            out_img[i][j][2] = C
    return out_img

if __name__ == "__main__":
    in_img, row, col = image_handler()
    out_img = convert_to_CMY()
    show_result_image(out_img)