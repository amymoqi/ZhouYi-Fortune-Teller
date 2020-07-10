# **********************************************************************************************************************
# Abacus automatically using ZhouYi thm
# **********************************************************************************************************************
import random


# -----------------------------------------------------------------------------------------------------------------------
def abacus() -> list:
    # random = 1为阳， = 0 为阴。
    # 每轮算三次，一共算六轮
    l = []
    count = 0
    for i in range(6):
        print("第" + str(i + 1) + "次: ")
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


def convert_to_code(lst: list) -> int:
    """
    convert this gua to code
    :param lst:
    :return:
    """
    count = 0
    length = len(lst)
    for i in range(length):
        if lst[i] % 2 != 0:
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
    for i in range(1, len(lines)):
        if lines[i].startswith('第'):
            gua.append(s)
            s = ''
        s = s + lines[i]
    gua.append(s)
    return gua


def split_info(gua: str) -> list:
    lst = gua.split('\n')
    format_lst = []
    s = ''
    for i in range(1, len(lst)):
        if lst[i].startswith("【"):
            format_lst.append(s)
            s = ''
        s = s + lst[i - 1]
    format_lst.append(s + lst[-1])
    # print(format_lst)
    return format_lst


def dong_yao(l: list) -> int:
    """
    return negative number if we should see the specific 动卦, return positive number if gua will be changed, return zero
    if no 动卦
    :param l: list from abacus
    :return:
    """
    dong_index = []
    jing_index = []
    for i in range(len(l)):
        if l[i] == 3 or l[i] == 0:
            dong_index.append(i+1)
        else:
            jing_index.append(i+1)

    ## return based on how many dong yao
    # 如果没有动爻，就看卦辞
    if len(dong_index) == 0:
        return 0
    # 如果有一个动爻，就看动爻的爻辞，如果两个动爻，就看上面动爻的爻辞，index越小越在上面
    elif len(dong_index) == 1 or len(dong_index) == 2:
        return dong_index[0]*(-1)
    elif len(dong_index) == 3:
        return dong_index[1]*(-1)
    elif len(dong_index) == 4:
        return jing_index[1]*(-1)
    elif len(dong_index) == 5:
        return jing_index[0]*(-1)
    else:
        for i in range(len(l)):
            if l[i]%2 == 0:
                l[i] = 1
            else:
                l[i] = 2
        return convert_to_code(l)


# -----------------------------------------------------------------------------------------------------------------------
# main program
print("start: thinking of something that is going to happen in the future.")
print("起卦：")
lst = abacus()  # list of int, record info of 动爻

print("解卦: ")
code = convert_to_code(lst)
num_dong = dong_yao(lst)
if num_dong > 0:
    code = num_dong

# deal with file
gua = read_from_file()  # all 64 gua from file

# find specific info(gua)
this_gua = gua[code]
gua_list = split_info(this_gua)

print(gua_list[0])  # print title
# print lines
if num_dong >= 0:
    print(gua_list[1])
    print(gua_list[2])
if num_dong < 0:
    print(gua_list[(7+num_dong)*2 + 1])
    print(gua_list[(7+num_dong)*2 + 2])

# print reference
print("Reference: ")
print("https://www.douban.com/group/topic/42705779/")
print("https://zhuanlan.zhihu.com/p/27880554")
