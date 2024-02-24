import cv2

def get_vid_source(vid_url):
    '''determine if the video source is a file or a camera stream or a url stream'''
    vid_type = 'unknown'
    if vid_url.isdigit():
        # camera stream from the machine
        vid_type = 'cam'
    elif vid_url.startswith('http') or vid_url.startswith('rtsp'):
        vid_type = 'url'
    elif vid_url.endswith('.mp4') or vid_url.endswith('.avi'):
        vid_type = 'file'

    '''get video source'''
    cap = cv2.VideoCapture(vid_url)
    return cap, vid_type

def capture_frames(cap, vid_type):
    # if the video source is a file, check if the video has ended
    ret, frame = cap.read()
    while ret:
        ret, frame = cap.read()
        yield frame

def close_vid(cap):
    '''release video source'''
    cap.release()