import cv2
import argparse
import pytesseract


def get_fps(video_cap):
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver) < 3:
        fps = video_cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print(
            "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video_cap.get(cv2.CAP_PROP_FPS)
        print(
            "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    return fps


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple OCR on videos')
    parser.add_argument('-f', '--file_dir', required=True,
                        help='Video file directory')
    args = parser.parse_args()

    video_cap = cv2.VideoCapture(args.file_dir)
    get_fps(video_cap)
