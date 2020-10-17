import cv2
import argparse
import glob
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os


def read_fonts(folder, size=30):
    fonts_extend = ['.ttf', '.otf']
    fonts_list = []
    for i in fonts_extend:
        fonts_list += glob.glob(folder + "/*" + i)
    # print(fonts_list)
    print("在{}中, 找到{}个字体".format(folder, len(fonts_list)))

    #fonts = [[ImageFont.truetype(i, size, encoding='utf-8'), i] for i in fonts_list]
    return fonts_list


def read_video_list(folder):
    video_extend = ['.flv', '.avi', '.mkv', '.mp4']
    videos = []
    for i in video_extend:
        videos += glob.glob(folder + "/*" + i)
    print("在{}中, 找到{}个视频".format(folder, len(videos)))
    return videos


def draw_text(img, x, y, txt, font, color=(0, 255, 255)):
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    # 第一个参数是文字的起始坐标，第二个需要输出的文字，第三个是字体颜色，第四个是字体类型
    draw.text((x, y), txt, color, font=font)

    # PIL图片转cv2
    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    return img


def main():
    video_folder = args.video_folder
    fonts_folder = args.fonts_folder
    np.random.seed(100)

    fonts_list = read_fonts(fonts_folder)
    img_list = glob.glob("/media/ming/DATA1/dataset/coco2017/images/val2017/*.jpg")

    if 1:
        for img_p in img_list:
            frame = cv2.imread(img_p)

            size = np.random.randint(10, 60)
            font_file = fonts_list[np.random.randint(len(fonts_list))]
            print(font_file)
            txt = "大家好,这是一个示例." + font_file
            color = (0, 255, 255)
            x, y = 30, 30

            font = ImageFont.truetype(font_file, size, encoding="utf-8")

            frame = draw_text(frame, x, y, txt, font, color)
            cv2.imwrite("result/"+os.path.basename(img_p), frame)
            #cv2.namedWindow("image", 0)
            #cv2.imshow('image', frame)
            #k = cv2.waitKey(0)

            #if k == 27:
            #    exit()

        #cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Genereate Synthetic Scene-Text Images')
    parser.add_argument('--vis', action='store_true', dest='viz', default=False,
                        help='flag for turning on visualizations')
    parser.add_argument('--fonts_folder', type=str, default="./fonts/chinese_fonts")
    parser.add_argument('--video_folder', type=str, default='/media/ming/DATA2/video/bilibili_video/1')
    args = parser.parse_args()
    main()
