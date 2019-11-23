# --*-- coding:utf-8 --*--
# 本文件中的print语句均为测试用语句，取消注释查看效果
# Pengyu Xiao 20191031

import sys
from HuffmanTree import Node, LeafNode, BranchNode, HuffmanTree, buildHuffmanTree
from Compress import buildTreeList
import os
import six
import time

def returnInt(dllen, dllist):
    length = 0 
    for i in range(dllen):
        length += (dllist[i] * (256**i))
    return length

def decompressFile(infile,outfile):
    time1=time.time()
    reader = os.open(infile,flags=os.O_BINARY|os.O_RDONLY)
    st_size = os.stat(reader)[6]#字节数
    # print(st_size)
    bytes_data = os.read(reader,st_size)#待转存

    time2=time.time()
    # 开始恢复头部信息
    # 读取字典长度
    returnlist = []
    h=bytes_data[0]
    for i in range(h):
        returnlist.append(bytes_data[i+1])

    dictlength = returnInt(h, returnlist)

    # 读取头部中的频率表
    counter = 0
    readcount = 0

    counter += dictlength
    readcount += h+1

    dict1 = {}
    while counter>0:
        charh = 0
        charreturn = []
        freqh =0
        freqreturn = []
        
        charh = bytes_data[readcount] # 读字节长度
        readcount += 1
        for i in range(charh):
            charreturn.append(bytes_data[readcount+i])
        readcount += charh
        char = returnInt(charh, charreturn)

        freqh = bytes_data[readcount]
        readcount += 1
        for i in range(freqh):
            freqreturn.append(bytes_data[readcount+i])
        readcount += freqh
        freq = returnInt(freqh, freqreturn)    
        dict1[char] = freq
        counter -= 1

    headlen = -1
    headlen += readcount
    
    # 重建Huffman树，这里直接使用Compress.py写好的函数和语句
    filetrees = []
    buildTreeList(dict1, filetrees)
    treeA = buildHuffmanTree(filetrees)
    treeA.traverseTree(treeA.getRoot(), '', dict1)

    output = open(outfile, 'wb')

    # 解压缩是压缩的逆过程
    outcode = ''
    node1 = treeA.getRoot()
    for i in range(readcount,st_size-2):
        char1 = bytes_data[i]
        for j in range(8):
            if char1&128:
                outcode = outcode + '1'
            else:
                outcode = outcode + '0'
            char1 = char1<<1
        while len(outcode) > 0:
            if node1.judgeLeaf():
                out = six.int2byte(node1.getChar())
                output.write(out)
                node1 = treeA.getRoot()

            if outcode[0] == '1':
                node1 = node1.getRight()
            else:
                node1 = node1.getLeft()
            outcode = outcode[1:]

    # [-2]位为最后一位位数，[-1]位为补全的码，现在重新还原
    lastbit = bytes_data[-2]
    filled = bytes_data[-1]
    lastcode = ''
    for j in range(8):
            if filled&128:
                lastcode = lastcode +'1'
            else:
                lastcode = lastcode + '0'
            filled = filled<<1
    lastcode = lastcode[0:lastbit]  

    while len(lastcode) > 0:
            if node1.judgeLeaf():
                lastout = six.int2byte(node1.getChar())
                output.write(lastout)
                node1 = treeA.getRoot()

            if lastcode[0] == '1':
                node1 = node1.getRight()
            else:
                node1 = node1.getLeft()
            lastcode = lastcode[1:]

    if node1.judgeLeaf():
        last1 = six.int2byte(node1.getChar())
        output.write(last1)
        currnode = treeA.getRoot
            
    time3 =time.time()
    output.close()
    return time3-time1,time3-time2,headlen
