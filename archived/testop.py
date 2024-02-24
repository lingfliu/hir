import sys
import cv2
import os
from sys import platform

# Import Openpose (Windows/Ubuntu/OSX)
dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    # Windows Import
    if platform == "win32":
    	# 如果在visual studio上编译的时候使用的是Release模式，把Debug换成Release
        os.environ['PATH'] = os.environ['PATH'] + ';' + 'E:/program_v1/hir/posers/OpenposeIID/config/Debug;' + 'E:/program_v1/hir/posers/OpenposeIID/config/bin;'
        import pyopenpose as op
    else:
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append('../../python')
        from openpose import pyopenpose as op
except ImportError as e:
    print(
        'Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

def get_body_connections(body_keypoints, pose_classes):
    body_connections = []

    # 手动指定骨骼连接
    # 可以根据需求进行修改
    connections = [
        (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8),
        (8, 9), (9, 10), (10, 11), (8, 12), (12, 13), (13, 14),
        (1, 0), (0, 15), (15, 17), (0, 16), (16, 18), (14, 19),
        (19, 20), (14, 21), (11, 22), (22, 23), (11, 24)
    ]

    for keypoints in body_keypoints:
        connection = []
        for connection_pair in connections:
            if (keypoints[connection_pair[0]][2] > 0.1 and
                    keypoints[connection_pair[1]][2] > 0.1):
                connection.append((pose_classes[connection_pair[0]],
                                    pose_classes[connection_pair[1]]))
        body_connections.append(connection)

    return body_connections[0]

class Openpose2d:
    def __init__(self):
        pass

    def output(self, dataset):
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        #
        # os.environ['PATH'] = os.environ['PATH'] + ';' + dir_path + './bin;'
        # import pyopenpose as op
        # 参数设置
        params = dict()
        params["model_folder"] = r"E:\program_v1\hir\posers\OpenposeIID\config\models"
        # 修改分辨率
        params["net_resolution"] = "256x192"
        # 修改参数，默认25个关节
        # params["model_pose"] = "DODY_25"
        # params["model_pose"] = "COCO"

        opWrapper = op.WrapperPython()
        opWrapper.configure(params)
        opWrapper.start()

        # 获取各个关节名称的列表
        pose_classes = op.getPoseBodyPartMapping(op.PoseModel.BODY_25)
        # 图片处理
        datum = op.Datum()
        # image_path = r'E:\program_v1\hir\posers\OpenposeIID\examples\COCO_val2014_000000000192.jpg'
        imageToProcess = dataset
        datum.cvInputData = imageToProcess
        opWrapper.emplaceAndPop(op.VectorDatum([datum]))
        cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", datum.cvOutputData)
        cv2.waitKey(0)
        # 将每个人的关节点信息放在一个列表中
        pos_frame = []
        for idx, person in enumerate(datum.poseKeypoints):
            keypoints = []
            for part_idx, part_coords in enumerate(person):
                part_name = pose_classes[part_idx]
                keypoints.append([part_coords[0], part_coords[1], part_coords[2]])
            pos_frame.append(keypoints)
        # 输出骨骼连接信息
        hierarchy = get_body_connections(pos_frame, pose_classes)
        return pos_frame, hierarchy

# 原始方法
'''def Openpose2d_1(image_path):
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    #
    # os.environ['PATH'] = os.environ['PATH'] + ';' + dir_path + './bin;'
    # import pyopenpose as op
    #参数设置
    params = dict()
    params["model_folder"] =r"E:\program_v1\hir\posers\OpenposeIID\config\models"
    #修改分辨率
    params["net_resolution"] = "256x192"
    #修改参数，默认25个关节
    # params["model_pose"] = "DODY_25"
    # params["model_pose"] = "COCO"

    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    #获取各个关节名称的列表
    pose_classes = op.getPoseBodyPartMapping(op.PoseModel.BODY_25)
    #图片处理
    datum = op.Datum()
    imageToProcess = cv2.imread(image_path)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", datum.cvOutputData)
    cv2.waitKey(0)
    #将每个人的关节点信息放在一个列表中
    pos_frame = []
    for idx, person in enumerate(datum.poseKeypoints):
        keypoints = []
        for part_idx, part_coords in enumerate(person):
            part_name = pose_classes[part_idx]
            keypoints.append([part_coords[0], part_coords[1], part_coords[2]])
        pos_frame.append(keypoints)
    #输出骨骼连接信息
    hierarchy = get_body_connections(pos_frame, pose_classes)
    return pos_frame, hierarchy'''