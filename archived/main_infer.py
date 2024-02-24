"""inference framework"""
import sys
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
sys.path.append(r'G:\works for study\py_program\hir\detectors\Yolov5_StrongSORT_OSNet')


"""TODO: 将以下工具补齐"""
from archived.media_tools import get_media_type, ImageAnnotator

from archived import media_tools

"""TODO: 将以下框架补齐"""
from archived.detectors import YoloDetector
from posers.OpenposeIID.openpose.testop import Openpose2d
from posers import StandardSkeleton
# from preprocess import SkeletonPreprocess, MotionPreprocess # 骨骼预处理，运动预处理
# from hir_analyzer import LocomotionClassifier # 运动分类器

"""global variable definition"""
media_source = "detectors/media/video.avi"
detector = YoloDetector()
pose_estimator = Openpose2d()
pose_formatter = StandardSkeleton()
# motion_classifier = LocomotionClassifier()
# skel_preprocess = SkeletonPreprocess()
# motion_preprocess = MotionPreprocess()


if __name__ == '__main__':

    if get_media_type(media_source) == 'video':

        # dataset = (path, im, im0s, vid_cap, s)
        # im是yolo需要的处理后的图像数据，im0s是原始图像数据（np(1280, 720, 3)）
        data_array = detector.load_data(media_source)

        detect_frames = detector.trace(dataset)

        # TODO: 显示检测框画面，参考YOLO_StrongSort

        pos_frames = []

        #hierarchy为骨骼连接信息，详细格式参考hir-dataloader项目
        hierarchy = None
        # 该数据通过遍历取出
        for frame_idx, (path, im, im0s, vid_cap, s) in enumerate(data_array):
        
            pos_frame, hierarchy = pose_estimator.output(im0s) # openpose输入原始图像数据
            # print(pos_frame, hierarchy)
            # pos_frame, hierarchy = pose_formatter.format(pos_frame, hierarchy) # 骨骼预处理
            # pos_frame = skel_preprocess(pos_frame, hierarchy) # 骨骼预处理
            # pos_frames.append(pos_frame)
            # TODO: 在帧图像上显示骨骼检测结果

        # pos_frames = motion_preprocess.filter(pos_frames, hierarchy) # 运动预处理

        # result = motion_classifier.classify(pos_frames)

    else:
        print("stream not supported yet")
