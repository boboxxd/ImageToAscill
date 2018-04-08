#!/usr/bin/python
#coding:utf-8
from PIL import Image;
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type=int,default=60)
parser.add_argument('--height',type=int,default=40)

#获取参数
args=parser.parse_args()
IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output



#使用灰度值公式将像素的rgb值映射到灰度值
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^'`.")

#将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
	if alpha ==0:
		return ' '
	length=len(ascii_char)
	gray=int(0.2126*r+0.7152*g+0.0722*b)
	unit = (256.0+1)/length
	return ascii_char[int(gray/unit)]

if __name__ == '__main__':
	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

	txt =''
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
			#getpixel 获取某个像素位置的值
		txt+= '\n'
	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open('output.txt','w') as f:
			f.write(txt)
