# --*-- coding:utf-8 --*--
# 本文件中的print语句均为测试用语句，取消注释查看效果
# Pengyu Xiao 20191031

# 基类结点定义
class Node(object):
    def __init__(self, freq=0, leafflag=0): # 初始化自带频度值和叶子结点flag
        self.freq = freq
        self.leafflag =leafflag

    def getFrequency(self):
        return self.freq

    def judgeLeaf(self):# 判断是叶还是分支
        if self.leafflag == 0:
            return True
        else:
            return False
    def getRoot(self): # 这个函数是考虑到类可用性完整性做的补充函数，防止结点建树和默认建树时报错
        return self

    
# 子类定义
# 叶结点
class LeafNode(Node):
    def __init__(self, freq=0 ,char=0):
        super().__init__()
        self.leafflag = 0
        self.char = char
        self.freq += freq # +=方便带值初始化
        
    # 私有方法
    def getChar(self):
        return self.char
    
    
# 分支结点
class BranchNode(Node):
    def __init__(self, left = LeafNode(),right = LeafNode()): # 这么写是为了防止默认定义报错 
        super().__init__()
        self.leafflag = 1
        self.left = left
        self.right = right
        self.freq += left.getFrequency()+right.getFrequency()
        
    # 私有方法
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


# Huffman树的类定义
class HuffmanTree(object):
    def __init__(self, nodeflag=0, char=0, freq=0, leftT = LeafNode(), rightT = LeafNode()):
        if nodeflag == 0:
            self.root = LeafNode(freq,char)
        else:
            self.root = BranchNode(leftT.getRoot(), rightT.getRoot())

    def getRoot(self):
        return self.root

    def getFrequency(self):
        return self.root.getFrequency()

    def traverseTree(self, root, code, dict0):
        if root.judgeLeaf():
            dict0[root.getChar()] = code
            # 打印编码表，取消下一行注释则打印
            # print(("char = %c, freq = %d,  code = %s") % (chr(root.getChar()), root.getFrequency(), code))
            return True
        else:
            self.traverseTree(root.getLeft(), code+'0', dict0)
            self.traverseTree(root.getRight(), code+'1', dict0)


# 通用的结点列表建树函数定义
def buildHuffmanTree(treelist):
    while len(treelist) >1:
        treelist.sort(key=lambda x:x.getFrequency()) # 按频度排序
        mintree1 = treelist[0]
        mintree2 = treelist[1]
        newtree = HuffmanTree(1,0,0,mintree1, mintree2)
        treelist =treelist[2:]
        treelist.append(newtree)
    return treelist[0]


