import numpy as np
import os
import sys
sys.path.append(r'D:\Github\hir\detectors\Yolov5_StrongSORT_OSNet\yolov5')
from archived.detectors import Hir_Yolo

track_method = 'ocsort'
model_dir = ''
model_name = 'yolov5x'


# class Hir_Yolo:
#     def __init__(self, yolo_weights, track_method=track_method, device='0', slice_enabled=False):
#         pass
#
#     def interface_people(self, source):
#
#         outputs_frame1 = np.array([[420, 70, 458, 214, 2, 0, 0.52752],
#                                    [1189, 20, 1238, 174, 1, 0, 0.56325]])
#         outputs_frame2 = np.array([[430, 92, 467, 231, 2, 0, 0.45148],
#                                    [1200, 42, 1251, 194, 1, 0, 0.58925]])
#         outputs = [outputs_frame1, outputs_frame2]
#
#         return outputs
tracker = Hir_Yolo(yolo_weights=os.path.join(model_dir, model_name) + '.pt')

class YoloDetector:
    def __int__(self):
        pass

    def detect(self, frame):
        # 将每一个frame的所有box(x1, y1, x2, y2, id, class)->(id, class, x1, y1, x2, y2)
        return [
            {
                'id': box[4],
                'class': box[5],
                'x1': box[0],
                'y1': box[1],
                'x2': box[2],
                'y2': box[3]
            } for box in frame
        ]

    def trace(self, dataset):
        # 返回的outputs = (w, h, n_frame, outputs)
        outputs = tracker.interface_people(dataset)

        return [self.detect(frame) for frame in outputs[-1]] # outputs最后一个参数是所有box数据[all_frame, one_frame_all_box, (x1, y1, x2, y2, id, class)]

    def load_data(self, media_source):
        return tracker.load_video(media_source) #从yolo模型中分离出的数据读取方法


if __name__ == '__main__':
    # media_source = "media/video.avi"
    # yolo_test = YoloDetector()
    # detect_frames = yolo_test.trace(media_source)
    # print(detect_frames)
    tracker = Hir_Yolo(yolo_weights=os.path.join(model_dir, model_name) + '.pt')
    w, h, n_frame, outputs = tracker.interface_people(dataset)