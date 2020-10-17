import cv2
import argparse
import glob
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def read_fonts(folder, size=30):
    fonts_extend = ['.ttf', '.TTF', '.otf']
    fonts_list = []
    for i in fonts_extend:
        fonts_list += glob.glob(folder + "/*" + i)
    # print(fonts_list)
    print("在{}中, 找到{}个字体".format(folder, len(fonts_list)))

    fonts = [[ImageFont.truetype(i, size, encoding='utf-8'), i] for i in fonts_list]
    return fonts


def read_video_list(folder):
    video_extend = ['.mp4', '.flv', '.avi', '.mkv']
    videos = []
    for i in video_extend:
        videos += glob.glob(folder + "/*" + i)
    print("在{}中, 找到{}个视频".format(folder, len(videos)))
    return videos


def draw_text(img, font):
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    # 第一个参数是文字的起始坐标，第二个需要输出的文字，第三个是字体颜色，第四个是字体类型
    draw.text((700, 450), font[1], (0, 255, 255), font=font[0])

    # PIL图片转cv2
    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    return img


def main():
    video_folder = args.video_folder
    fonts_folder = args.fonts_folder
    np.random.seed(100)

    fonts = read_fonts(fonts_folder)
    video_list = read_video_list(video_folder)

    for video in video_list:
        print("reading: {}".format(video))
        cap = cv2.VideoCapture(video)

        cv2.namedWindow("image", 0)
        index = 0
        while cap.isOpened():
            print(index)
            ret, frame = cap.read()

            font = fonts[np.random.randint(len(fonts))]
            frame = draw_text(frame, font)
            cv2.imshow('image', frame)
            k = cv2.waitKey(0)
            index += 1
            if k == 27:
                exit()

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Genereate Synthetic Scene-Text Images')
    parser.add_argument('--vis', action='store_true', dest='viz', default=False,
                        help='flag for turning on visualizations')
    parser.add_argument('--fonts_folder', type=str, default="./fonts/chinese_fonts")
    parser.add_argument('--video_folder', type=str, default='/media/ming/DATA2/video/bilibili_video/1')
    args = parser.parse_args()
    main()
