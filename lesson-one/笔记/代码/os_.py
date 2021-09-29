import os

# 获取当前的工作目录
print(os.getcwd())
# 创建目录,只能创建一层目录
# os.mkdir(os.getcwd() + '/test')
# os.mkdir(os.getcwd() + '/abc')
# # 创建多层目录
# os.makedirs(os.getcwd() + '/def/123')

# print(os.listdir(os.getcwd()))
# print(os.listdir('/'))
# .表示当前目录，..表示父级目录
print(os.path.abspath('..'))
# 相对路径 ./text.txt  ../test/abc.py
# 绝对路径 /Users/xxx/projects  c:\documents\readme.txt
# 目录分隔符： Windows: \  Mac和Linux /
cur_file = os.path.abspath(__file__)
# 判断“文件“是否存在
print(os.path.isfile(cur_file))
print(os.sep)
print(os.path.join(os.getcwd(), 'def', '123'))
print(os.path.dirname(cur_file))
print(os.path.basename(cur_file))
print(os.path.basename('/tmp/test'))