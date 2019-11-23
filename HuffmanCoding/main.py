# --*-- coding:utf-8 --*--
#本文件为主文件
#如果需要输出码表、频率表，请到/source文件夹下Compress.py和HuffmanTree.py
#Pengyu Xiao 20191112
import os
import sys
workdir = os.getcwd()
sourcedir =os.path.join(workdir,'source')
sys.path.append(sourcedir)
from Compress import compressFile
from Decompress import decompressFile


####################################################
#请在此处修改文件名和格式
#名字
name = "诺贝尔化学奖"
#格式
form = "txt"
#压缩文件格式
compform = "huf"
####################################################




#待压缩文件
infile = workdir+"\\files\\"+name+"."+form
#压缩后文件
comfile = workdir+"\\files\\"+name+"_压缩."+compform
#解压后文件
outfile = workdir+"\\files\\"+name+"_解压."+form

insize = os.path.getsize(infile)

print("待压缩文件名: ",infile)
print("压缩后文件名: ",comfile)
print("解压后文件名: ",outfile,"\n")

quitflag = 1

while quitflag:
    flag = 0
    while (flag==0):
        print("输入c进行压缩\n输入d进行解压\n输入q退出\n回车键确认，其它输入无效")
        get = input()
        if get == 'c':
            flag = 1
        else :
            if get == 'd':
                flag = 2
            else:
                if get == 'q':
                    flag = 3
                    quitflag = 0
    if (flag == 1):
        comptime = compressFile(infile,comfile)
        print("压缩完毕\n压缩操作总时间\t{} 秒".format(comptime[0])+"\n压缩时间\t{} 秒".format(comptime[1]))        
        print("原文件大小:\t {}b".format(insize)+"\n压缩文件大小:\t {}b".format(os.path.getsize(comfile)))
        print("码表长度:\t{} ".format(comptime[2])+"\n最大码字长度:\t{}".format(comptime[3])+"\n最小码字长度:\t{}".format(comptime[4]))
    if (flag == 2):
        decotime = decompressFile(comfile,outfile)
        print("解压完毕\n解压操作总时间\t{} 秒".format(decotime[0])+"\n解压时间\t{} 秒".format(decotime[1]))
        print("压缩文件大小:\t {}b".format(os.path.getsize(comfile))+"\n还原文件大小:\t {}b".format(os.path.getsize(outfile)))
        print("原内容压缩大小:\t{}b".format(os.path.getsize(comfile)- decotime[2]))
sys.exit()
