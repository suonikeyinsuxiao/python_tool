#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: opts.py
#Brief:  简单的介绍python中命令行参数的使用
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-25 15:19:24
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/suonikeyinsuxiao/python_tool
#############################################

'''
#简单的命令行参数
import sys
print("argv[0]={}".format(sys.argv[0]))
for i in range(1, len(sys.argv)):
    print("argv[{}]={}".format(i, sys.argv[i]))
'''

'''
解析命令行参数列表
getopt.getopt(args, options[, long_options])
args: 要解析的命令行参数列表。通常是sys.argv[1:],sys.argv[0]是脚本名,需要将其过滤掉.否则getopt()的返回值中将不包含(option,value)组成的列表
options: 短格式参数字符串，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
long_options: 长格式参数字符串，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
'''



import sys,getopt
opts, args = getopt.getopt(sys.argv[1:], "hi:o:",['help', 'inputfile=', 'outputfile='])
print(opts)
print(args)
for option,value in opts:
    if option in ("-h", '--help'):
        print("test.py -h|--help")
    elif option in ("-i", "--inputfile"):
        print("test.py -i <inputfile> --inputfile <inputfile>")
    elif option in ("-o", "--outputfile"):
        print("test.py -o <outputfile> --outputfile <outputfile>")



