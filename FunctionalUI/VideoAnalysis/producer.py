import threading
import cv2
import time


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        # thread
        self.ThreadRun = True
        

    def run(self):
        '''
          线程处理
        '''
        self.Stop()
        # self.video_capture = cv2.VideoCapture(1)
        while self.ThreadRun:
            ret, frame = self.video_capture.read()
            if not ret:
                print("Video Read Failed")
                break
            if 27 == cv2.waitKey(30):
                print("Esc Pressed,Quit Video")
                break  
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            print(h, w, ch)
            # bytes_per_line = ch * w
            # q_img = qg.QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            # pixmap = QPixmap.fromImage(q_img)

    def Stop(self):
        self.ThreadRun = False
    def Start(self):
        self.start()