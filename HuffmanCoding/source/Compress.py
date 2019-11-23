# --*-- coding:utf-8 --*--
# 本文件中的print语句均为测试用语句，取消注释查看效果
# Pengyu Xiao 20191031

import sys
from HuffmanTree import Node, LeafNode, BranchNode, HuffmanTree, buildHuffmanTree
import os
import six
import time



def printFreqList(dict0):# 输出频率表函数
    print('char\tfrequency')
    for ch in dict0.keys():
        print(ch,' \t',dict0[ch])


def buildFreqList(asize, adata, dict0):
    for i in range(asize):
        char = adata[i]
        if char in dict0.keys():
            dict0[char] += 1
        else:
            dict0[char] = 1
    dictlen = len(dict0.keys())
    # 输出频率表函数，取消下一行注释则输出频率表
    #printFreqList(dict1)
    return dictlen
    
def buildTreeList(dict0, treelist0):
    for ch in dict0.keys():
        leaftree = HuffmanTree(0, ch, dict0[ch], None, None)#注意参数char和freq是int
        treelist0.append(leaftree)
    
def turnBytes(length):#整数转化为字节数+逆序字节列表的形式存进去
    bytenum =1
    flag = 1
    store = []
    while(flag):
        if length >= (256): # 例如：258 = 2(bytes数) + [2,1]   (因为1*256+2=258)
            bytenum +=1
            store.append((length-256)%256)
            length = 1+int((length-256)/256)
        else:
            store.append(length)
            flag = 0
    return bytenum, store

def compressFile(infile,outfile):
    time1=time.time()#开始读取的时间节点
    reader = os.open(infile,flags=os.O_BINARY|os.O_RDONLY)
    st_size = os.stat(reader)[6]#字节数
    #print(st_size)
    bytes_data = os.read(reader,st_size)#待转存
    
    output = open(outfile,'wb')
    time2=time.time()#开始压缩的时间节点
    dict1 = {}
    dictlength = buildFreqList(st_size, bytes_data, dict1)

    filetrees = []
    buildTreeList(dict1, filetrees)

    dllen = 0
    dllist = []
    dllen , dllist = turnBytes(dictlength)

    #头部写入
    output.write(six.int2byte(dllen)) # 压缩文件[0]是dllen，
    for i in range(dllen):      # 跟着dllen字节是从低到高的dllist
        output.write(six.int2byte(dllist[i]))

    dllen1 = 0
    dllist1 = []
    co =0
    # 接下来是char + freq的组合
    for key in dict1.keys():
        dllen ,dllist = turnBytes(key) # 存入key
        output.write(six.int2byte(dllen))
        for i in range(dllen):
            output.write(six.int2byte(dllist[i]))
        dllen1 ,dllist1 = turnBytes(dict1[key])# 存入dict1[key]
        output.write(six.int2byte(dllen1))
        for i in range(dllen1):      
            output.write(six.int2byte(dllist1[i]))
        co += 1


    treeA = buildHuffmanTree(filetrees)
    treeA.traverseTree(treeA.getRoot(), '', dict1)


    #文件压缩
    outcode = ''
    maxclen = 0
    minclen = 99
    for i in range(st_size):
        key =bytes_data[i]
        maxclen = max(maxclen,len(dict1[key]))
        minclen = min(minclen,len(dict1[key]))
        outcode += dict1[key]
        out = 0
        while len(outcode)>8:
            for j in range(8):
                out = out<<1
                if outcode[j] =='1':
                    out = out|1
            outcode = outcode[8:]
            output.write(six.int2byte(out))
            out = 0

    #最后不满8位
    #写入了1位剩余长度(即[-2]位)
    output.write(six.int2byte(len(outcode)))
    out = 0
    for i in range(len(outcode)):
        out = out<<1
        if outcode[i] == '1':
            out = out|1
    for i in range(8-len(outcode)):
        out = out<<1
    output.write(six.int2byte(out))
    time3=time.time()#结束的时间节点
    output.close()
    os.close(reader)
    return time3-time1,time3-time2,dictlength,maxclen,minclen

