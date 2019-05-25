import os
import shutil as fm
import sys
import time

def CEF(path):
    files = os.listdir(path)  # 获取路径下的子文件(夹)列表
    for file in files:
        if os.path.isdir(file):  # 如果是文件夹
            if not os.listdir(file):  # 如果子文件为空
                os.rmdir(file)  # 删除这个空文件夹
        elif os.path.isfile(file):  # 如果是文件
            if os.path.getsize(file) == 0:  # 文件大小为0
                os.remove(file)  # 删除这个文件
                
print ("Farrangement 文件整理 [版本 0.9beta]")
print ("遵循GPLv3协议")
print ("作者: wzy2006 博客: wzy2006.github.io")
try:
    os.mkdir("文档")
    os.mkdir("视频")
    os.mkdir("代码")
    os.mkdir("图片")
    os.mkdir("压缩")
    os.mkdir("音乐")
    os.mkdir("其他")
except BaseException:
    i=0
path="C:\\Users\\Administrator\\Desktop\\"
print("\n开始整理")
lis=list(os.walk(path))[0][2]
for i in lis:
    ftype=(os.path.splitext(i)[1])
    if ftype=='.doc' or ftype == '.docx' or ftype == '.wps' or ftype =='.et' or ftype =='.xls' or ftype =='.xlsx' or ftype=='.ppt' or ftype =='.pptx' or ftype=='.dps' or ftype=='.txt'or ftype==".pdf":
        fm.move(path+i,"C:\\Users\\Administrator\\Desktop\\文档\\"+i)
    elif ftype=='.jpg' or ftype==".jpeg" or ftype==".png" or ftype==".gif" or ftype==".bmp" or ftype==".pcx" or ftype==".tiff":
        fm.move(path+i,"C:\\Users\\Administrator\\Desktop\\图片\\"+i)
    elif ftype==".zip" or ftype==".rar" or ftype==".gz" or ftype==".tar" or ftype==".7z" or ftype==".iso":
         fm.move(path+i,"C:\\Users\\Administrator\\Desktop\\压缩\\"+i)
    elif ftype==".mp4" or ftype==".mkv" or ftype==".mov" or ftype==".rm" or ftype==".rmvb" or ftype==".wmv" or ftype==".avi":
        fm.move(path+i,"C:\\Users\\Administrator\\Desktop\\视频\\"+i)
    elif ftype==".mp3" or ftype==".wmv" or ftype==".wav" or ftype==".flac":
        fm.move(path+i,"C:\\Users\\Administrator\\Desktop\\音乐/"+i)
    elif ftype==".java" or ftype==".c" or ftype==".cpp" or ftype==".exe" or ftype==".dll" or ftype==".lib" or ftype==".dsp" or ftype==".dsw" or ftype==".cs" or ftype==".asp" or ftype==".aspx" or ftype==".php" or ftype==".jsp" or ftype==".go" or ftype==".py" or ftype==".pyc" or ftype==".asm" or ftype==".vbs" or ftype==".bat" or ftype==".cmd":
        fm.move(path+i,"C:\\Users\\Administrator\\Desktop\\代码\\"+i)
    else:
        fm.move(path+i,"C:\\Users\\Administrator\\Desktop\\其他\\"+i)
CEF('C:\\Users\\Administrator\\Desktop\\')


print("完成!")
time.sleep(5)
