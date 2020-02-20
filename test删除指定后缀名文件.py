import os
path = os.path.dirname(__file__)
filenames = os.listdir(path)
for file in filenames:
    if file.endswith(('eot', 'woff')):
        os.remove(os.path.join(path, file))
print(filenames)


# import os
# #删除一个目录文件中的某些特定后缀名文件
# def del_files(path):
#   for root , dirs, files in os.walk(path):
#     for name in files:
#       if name.endswith(a):
#         os.remove(os.path.join(root, name))
#         print ("删除文件: " + os.path.join(root, name))
# #删除空目录
# def delnull(dirr):
#     if os.path.isdir(dirr):
#         for p in os.listdir(dirr):
#             d  = os.path.join(dirr,p)
#             if (os.path.isdir(d) == True):
#                 delnull(d)
#     if not os.listdir(dirr):
#         os.rmdir(dirr)
#         print('移除空目录: ', dirr)
# # 输入相应的内容然后把参数传入到函数中
# if __name__ == "__main__":
#     print("请输入想要删除的文件后缀:")
#     a=input()
#     print("请输入要删除的文件的根目录")
#     b=input()
#     path = b
#     del_files(path)
#     print("输入要移除的空目录")
#     c=input()
#     delnull(c)
