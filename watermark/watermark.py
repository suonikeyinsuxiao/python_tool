#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: watermark.py
#Brief: 给图片水印工具
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-25 11:08:25
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/suonikeyinsuxiao/python_tool
#############################################
import time
import sys,getopt

try:
    from PIL import Image, ImageDraw, ImageFont, ImageEnhance
except ImportError:
    import Image, ImageDraw, ImageFont, ImageEnhance

usage = """test.py [option] [value]
test.py  -i <inputfile> | --inputfile <inputfile> 
         -o <outputfile> | --outputfile <outputfile> 
         --text <string>
        """

def add_text(img, text, font, outfile, angle=45):
    #starttime = time.time()
    # make a blank image for the text, initialized to transparent text color
    img_txt = Image.new('RGBA', img.size, (255,255,255,0))

    # get a drawing context
    d = ImageDraw.Draw(img_txt)
    # draw text, color red, full opacity
    d.text((0,img.height/2), text, font=font, fill=(255,0,0,255))

    img_txt = img_txt.rotate(angle, Image.BICUBIC)

    outfile = outfile + time.strftime("_%Y%m%d%H%M%S") + ".png"
    Image.alpha_composite(img, img_txt).save(outfile)
    #endtime = time.time()
    #print("水印方法执行时间:",endtime-starttime)


if __name__ == '__main__':
    inputfile = 'myself.jpeg'
    mytext='https://github.com/suonikeyinsuxiao/python_tool'
    outfile='myself'
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:",['help', 'inputfile=', 'text=', 'outputfile='])
    for option,value in opts:
        if option in ("-h", '--help'):
            print(usage)
            exit(0)
        elif option in ('-i', '--inputfile'):
            inputfile = value
        elif option in ('--text'):
            mytext = value
        elif option in ('-o', '--outputfile'):
            outfile = value


    fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 20)
    image = Image.open(inputfile).convert('RGBA');
    add_text(image, mytext, fnt, outfile)
