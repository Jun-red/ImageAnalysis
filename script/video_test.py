import sys
import cv2

if __name__ == '__main__':
    print("hello world")
    video_capture = cv2.VideoCapture(1)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print('???')
            break

        cv2.imshow("test-video_cap", frame)
        i_K = cv2.waitKey(30) 
        if i_K == 27:
            print("ESC")
            break