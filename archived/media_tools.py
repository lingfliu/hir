import cv2
import matplotlib.pyplot as plt
from detectors import YoloDetector
IMG_FORMATS = 'bmp', 'dng', 'jpeg', 'jpg', 'mpo', 'png', 'tif', 'tiff', 'webp', 'pfm'  # include image suffixes
VID_FORMATS = 'asf', 'avi', 'gif', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'ts', 'wmv'  # include video suffixes


data_load = YoloDetector()

class ImageAnnotator:
    def __init__(self):
        pass




def get_media_type(media_source):

    type = media_source.split(sep='.')[-1]
    if type in VID_FORMATS:
        return 'video'
    else:
        return 'not_video'



if __name__ == '__main__':

    media_source = "detectors/media/video.avi"
    # type = get_media_type(media_source)
    frame = load_video(media_source)
    for i in range(len(frame)):
        plt.imshow(frame[i])
        plt.show()