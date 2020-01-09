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


def perform_ocr(crop):
    '''
    crop is a numpy array
    '''
    # ret, imgthresh = cv2.threshold(crop, 110, 255, cv2.THRESH_BINARY_INV)
    # imgthresh2 = cv2.adaptiveThreshold(crop_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    text = pytesseract.image_to_string(crop, lang="eng",
                                       config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')

    print('text: ', text)
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple OCR on videos')
    parser.add_argument('-f', '--file_dir', required=True,
                        help='Video file directory')
    args = parser.parse_args()

    video_cap = cv2.VideoCapture(args.file_dir)
    get_fps(video_cap)
    count = 0
    while (video_cap.isOpened()):
        ret, frame = video_cap.read()
        if ret == True:
            air_speed_crop = frame[222:248,190:240]
            timing_crop = frame[432:451, 63:200]
            cv2.imwrite("frame_{}.png".format(count), air_speed_crop)
            perform_ocr(air_speed_crop)
            count += 1
        else:
            break

    video_cap.release()
    cv2.destroyAllWindows()
