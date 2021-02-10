import cv2
import os
import argparse

def get_frame_from_video(video, output_dir, images_per_sec=1):
    video_name = os.path.splitext(os.path.split(video)[-1])[0]
    subfolder = os.path.join(output_dir, video_name)
    output_name = os.path.join(subfolder, video_name)

    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()

    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    fps = 30 if fps <= 0 else fps
    frame_counter = 0
    total_frame = 1
    while success:
        if total_frame * images_per_sec % fps == 0:
            cv2.imwrite(output_name + "_%d.jpg" % frame_counter, image)
            frame_counter += 1
        success, image = vidcap.read()
        total_frame += 1
    return subfolder


def get_frame_from_path(path, output_dir, images_per_sec=1, force_render=False):
    """
    force_render: render the frames even if there is an existing path of the subfolder
    """

    assert os.path.exists(path), "No such path: {}".format(path)
    vid_fm = (".flv", ".avi", ".mp4", ".3gp", ".mov", ".gif" ".webm", ".ts")

    video_paths = [video_name for video_name in os.listdir(path) if os.path.splitext(video_name)[-1] in vid_fm]
    for video in video_paths:
        video_name = os.path.splitext(video)[0]
        subfolder = os.path.join(output_dir, video_name)
        if not force_render and os.path.exists(subfolder):
            continue
        else:
            os.makedirs(subfolder, exist_ok=True)
            get_frame_from_video(os.path.join(path, video), output_dir, images_per_sec)
    print ('Video2Frames Completed')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Video to Frames')
    parser.add_argument('--img_per_sec', default=1, type=int, help='num of images to take per sec')
    parser.add_argument('--force_render', default=False, help='Convert all videos in path to frames')
    args = parser.parse_args()

    video_input = os.getenv('raw_video')
    output_dir = os.getenv('offline_annotation_repo')

    assert video_input != None, "Please set env var at /etc/environment"
    assert output_dir != None, "Please set env var at /etc/environment"
    
    get_frame_from_path(video_input, output_dir, images_per_sec=args.img_per_sec)