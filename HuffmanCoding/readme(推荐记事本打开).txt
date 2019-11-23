517030910220 肖鹏宇
信息论与编码大作业 HuffmanCoding 
说明文档


运行要求：
 Python 3.6
	
modules: six , sys , os (均为Python3自带库)



使用方法：编辑main.py中的文件名、格式名、压缩文件格式名，将
待压缩文件放在files文件夹下，运行main.py，按照指示输入c\d
，即可进行压缩和解压

文件夹结构

HuffmanCoding
	
	|
	main.py  主函数文件，使用算法请用Python3 IDLE或其它运行（而非命令行）
			|	
	|	files       存放待压缩和处理后文件的文件夹，请将文件放在此处             
	
	|
	|	（.idea、__pycache__   运行缓存和PyCharm缓存，无需关注）
	|
	|	source    源码文件夹
		     |	Compress.py        压缩函数文件
		     |	Decompress.py    解压函数文件
		     |	HuffmanTree.py   哈夫曼树类与结点类定义文件
		     |          （__init__.py       os、sys库的某些函数需要的空白定位文件，无需关注）

请注意：由于原文件自带编码，解压后未做还原，解压的docx等文件类型第一次打开之后，可能无法读取，这时Word会请求修复文件，请修复文件并另存为新文件，这个修复后文件与原文件完全相同。请见files文件夹下的 脑机接口新突破_修复.docx