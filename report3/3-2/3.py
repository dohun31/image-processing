"""
영상비전처리 과제 #2
201911900 백도훈 
3-2-3. RGB - YCbCr 변환 프로그램
"""
import cv2
import numpy as np

def image_handler():
    in_img = cv2.imread("/Users/dohun/Desktop/대학생 도훈이/3학년2학기/영비처/과제/lena_std.tif")
    row, col, _ = in_img.shape
    return in_img, row, col

def show_result_image(out_img):
    title = 'RGB-to-YCbCr'
    cv2.imshow(title, out_img)
    cv2.waitKey(0)

def convert_to_YCbCr():
    Y = np.copy(in_img[:, :, 0])
    Cb = np.copy(in_img[:, :, 0])
    Cr = np.copy(in_img[:, :, 0])
    tmp_img = np.float32(in_img)
    R, G, B = tmp_img[:, :, 2], tmp_img[:, :, 1], tmp_img[:, :, 0]
    for i in range(row):
        for j in range(col):
            Y[i][j] = 0.299 * R[i][j] + 0.587 * G[i][j] + 0.114 * B[i][j] 
            Cr[i][j] = (R[i][j] - Y[i][j]) * 0.713 + 128 
            Cb[i][j] = (B[i][j] - Y[i][j]) * 0.564 + 128
    return Y, Cb, Cr, cv2.merge((Y, Cr, Cb))

if __name__ == "__main__":
    in_img, row, col = image_handler()
    Y, Cb, Cr, out_img = convert_to_YCbCr()
    cv2.imshow('origin', in_img)
    cv2.imshow('Y', Y)
    cv2.imshow('Cb', Cb)
    cv2.imshow('Cr', Cr)
    cv2.imshow('result', out_img)
    cv2.waitKey(0)