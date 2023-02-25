"""inference framework"""


"""TODO: 将以下工具补齐"""
from media_tools import load_video, get_media_type, ImageAnnotator

"""TODO: 将以下框架补齐"""
from detectors import YoloDetect
from pose_estimator import Openpose3d
from preprocess import SkeletonPreprocess, MotionPreprocess # 骨骼预处理，运动预处理
from hir_analyzer import LocomotionClassifier # 运动分类器

"""global variable definition"""
media_source = "rtsp://localhost:7554/test.mp4"
detector = YoloDetect()
pose_estimator = Openpose3d()
motion_classifier = LocomotionClassifier()
skel_preprocess = SkeletonPreprocess()
motion_preprocess = MotionPreprocess()


if __name__ == '__main__':

    if get_media_type(media_source) == 'video':
        video = load_video(media_source)
        detect_frames = detector.trace(video)

        # TODO: 显示检测框画面，参考YOLO_StrongSort

        pos_frames = []
        hierarchy = None
        for frame in detect_frames:
            pos_frame, hierarchy = pose_estimator.estimate()
            pos_frame, hierarchy = skel_preprocess.normalize(pos_frame, hierarchy) # 骨骼预处理
            pos_frames.append(pos_frame)
            # TODO: 在帧图像上显示骨骼检测结果

        pos_frames = motion_preprocess.filter(pos_frames, hierarchy) # 运动预处理

        result = motion_classifier.classify(pos_frames)

    else:
        print("stream not supported yet")







