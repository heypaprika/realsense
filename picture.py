import pyrealsense2 as rs
import numpy as np
import cv2
import os
import pickle
# 사용법 :
# 키보드의 s key로 카메라로 비추고 있는 사진 캡처하여 저장.
# 키보드의 q key로 프로그램 종료.

config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

pipeline = rs.pipeline()
pipeline.start(config)

savepath = 'pic/saveimg_by_realsense/'
path, dirs, files = next(os.walk(savepath))
count=len(files)/2

while True:

    frames = pipeline.wait_for_frames()

    color_frame = frames.get_color_frame()
    color_image = np.asanyarray(color_frame.get_data())

    depth_frame = frames.get_depth_frame()
    depth_image = np.asanyarray(depth_frame.get_data())

    cv2.imshow('RealSense', color_image)
    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite(savepath+"%d.jpg"%(count), color_image)
        with open(savepath+"%d.pickle"%(count), 'wb') as file:
            pickle.dump(depth_image, file)
        print(str(int(count))+".jpg &",str(int(count))+".pickle file saved!")

        count += 1
    elif key == ord('q'):
        break
