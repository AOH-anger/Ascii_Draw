#coding=utf-8

from PIL import Image
import argparse

# 命令行输入参数的处理
parse = argparse.ArgumentParser()
parse.add_argument('file')
parse.add_argument('-o','--output')
parse.add_argument('--width',type = int,default = 80)
parse.add_argument('--height',type = int,default = 80)

# 获取参数
args = parse.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 设置字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    #  RGB--灰度值转换公式
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256.0 / length
    return ascii_char[int(gray/unit)]

def handle_image():

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('out.txt','w') as f:
            f.write(txt)


if __name__ == '__main__':
    handle_image()
