"""inference framework"""
import time
import cv2
import vid_source

# definining data source
vid_url = './resources/sample.S01E08.HD1080p.mp4'
# configurations
resize = (300, 300)

buff_size = 100
frame_buffed = []
detect_buffed = []

def component_detect(frame_buffed, frame_resized):
    # TODO implement the detection algorithm
    return  [
        {"class": "lhand", "confidence": 0.9, "bbox": [0, 0, 100, 100], "id": 1},
        {"class": "rhand", "confidence": 0.9, "bbox": [0, 0, 100, 100], "id": 1},
    ]

# should return the adjacency matrix of skeleton
def connect_component(detect):
    # TODO implement the connection algorithm
    return {}

def st_traj_matching(skeletons):
    return [(1,2), (2,3)]

def recog_single(motion):
    return 5, 0.9

def recog_hoi(motion):
    return 5, 0.9



if __name__ == '__main__':
    '''inference from video source'''
    cap, vid_type = vid_source.get_vid_source(vid_url)
    if vid_type == 'unknown':
        print('unknown video source')
        exit(0)
    elif vid_type == 'file':
        total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print('total frame: ', total_frame)
    elif vid_type == 'url':
        print('url video source')

    tic = time.time()
    dts = []
    for frame in vid_source.capture_frames(cap, vid_url):
        # do something with the frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # sleep 0.02 seconds
        toc = time.time()
        # get the time difference
        # dts.append(toc-tic)
        # if len(dts) > 1000:
        #     print("fps: ", 1/(sum(dts)/len(dts)))
        #     dts = []
        # print("time: ", toc-tic)
        # tic = toc

        # preprocessing
        frame_resized = cv2.resize(frame, resize)

        detect = component_detect(frame_buffed, frame_resized)
        frame_buffed.append(frame_resized)
        if len(frame_buffed) > buff_size:
            frame_buffed.pop(0)

        detect_buffed.append(detect)
        if len(detect_buffed) > buff_size:
            detect_buffed.pop(0)

        skeletons = connect_component(detect)

        matched = st_traj_matching(skeletons)

        # TODO generate human-object motion sequences
        motion = []

        for match in matched:
            skeleton,  obj = match
            if obj is None:
                # no interaction
                recog_single(motion)
            elif not obj.type == 'skeleton':
                # object to object interaction
                recog_hoi(motion)
            else: # skeleton to skeleton interaction
                recog_hoi(motion)

        # TODO draw results on frames

        # TODO save the results to a video file

    vid_source.close_vid(cap)


