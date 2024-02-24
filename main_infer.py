"""inference framework"""
import time
import cv2

# definining data source
vid_url = './resources/sample.S01E08.HD1080p.mp4'
import vid_source

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
        dts.append(toc-tic)
        if len(dts) > 1000:
            print("fps: ", 1/(sum(dts)/len(dts)))
            dts = []
        print("time: ", toc-tic)
        tic = toc
    vid_source.close_vid(cap)


