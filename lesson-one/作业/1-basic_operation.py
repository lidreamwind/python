import os
from os.path import join, getsize


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size


if __name__ == '__main__':
    path = r'E:\简历'
    size = getdirsize(path)
    print('There are %.3f' % (size / 1024 / 1024), 'Mbytes in E:\简历')