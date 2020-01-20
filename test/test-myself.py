import re

a = 'Customer'
b = '123'
regex = re.compile('^[a-z]+')
# print(regex.findall(a.lower()),'    ',len(regex.findall(a.lower())))
# print(regex.findall(b.lower()),'    ',len(regex.findall(b.lower())))


def kmfzgl(x):
    regex = re.compile('^[a-z]+')  # 过滤所有科目编号是字母的情况
    regex1 = re.compile('^[1-9]+')
    if(len(x)>3 and len(regex.findall(x.lower()))<1 and len(regex1.findall(x))>=1):
        if (x.__contains__('-')):
            return False
        else:
            return True
    return False

def format_flat(row):
    row = '{:.2f}'.format(row)
    print(row)

# format_flat(6.087782e+06)
def move_qcye(row):
    if(row[4:6]>'01' and row[4:6]<='12'):
        print(2)
move_qcye('201302')
