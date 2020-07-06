# **********************************************************************************************************************
# Abacus automatically using ZhouYi thm
# **********************************************************************************************************************
import random
########################################################################################################################
def abacus() -> list:
    # random = 1为阳， = 0 为阴。
    # 每轮算三次，一共算六轮
    l = []
    count = 0
    for i in range(6):
        print("第" + str(i+1) + "次: ")
        for a in range(3):
            bit = random.getrandbits(1)
            if bit == 1:
                count = count + 1
        l.insert(0, count)  # 要从下往上写
        if count == 1:
            print("阳爻 ———")
        elif count == 2:
            print("阴爻 — —")
        elif count == 3:
            print("动阳 ———")
        else:
            print("动阴 — —")
        count = 0
    return l


def convert_to_code(lst:list)->int:
    """
    convert this gua to code
    :param lst:
    :return:
    """
    count = 0
    length = len(lst)
    for i in range(length):
        if lst[i]%2 != 0:
            count = count + pow(2, length - 1 - i)
    return count

def read_from_file() -> list:
    """
    give a list, each item in the list is one gua, it is sorted by binary code
    :return:
    """
    file = 'Lib'
    f = open(file, 'r', encoding='utf8')
    lines = f.readlines()
    gua = []
    s = lines[0]
    for i in range(1,len(lines)):
        if lines[i].startswith('第'):
            gua.append(s)
            s = ''
        s = s + lines[i]
    gua.append(s)
    return gua

def split_info (gua: str) -> list:
    lst = gua.split('\n')
    format_lst = []
    format_lst.append(lst[0])  # append title
    for i in range(1, len(lst)):
        if lst[i].startswith("【"):


########################################################################################################################
# main program
print("start: thinking of something that is going to happen in the future.")
print("起卦：")
list = abacus()
print("解卦: ")
code = convert_to_code(list)
print(code)
gua = read_from_file() # all 64 gua from file
this_gua = gua[code]



#print("Reference: https://www.douban.com/group/topic/42705779/")
#https://zhuanlan.zhihu.com/p/27880554