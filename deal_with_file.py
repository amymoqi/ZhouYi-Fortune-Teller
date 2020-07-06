# **********************************************************************************************************************
# deal with Lib file for ZhouYi
# **********************************************************************************************************************

########################################################################################################################
def convert_to_num(lst: list) -> int:
    length = len(lst)
    count = 0
    for i in range(length):
        try:
            if lst[i] =='True':
                count = count + pow(2, length - 1 - i)
        except:
            print("cannot convert:" + lst[i])
    return count


########################################################################################################################
file = 'Lib'
f = open(file, 'r', encoding='utf8')

## there are blank lines in the original file, delete it.
# lines = f.readlines()
# f.close()
# lines = filter(lambda x: x.strip(), lines)

## add '[True, True, True, True, True, True]\n' before every Gua
# lines = f.readlines()
# i = 0
# while i < len(lines):
#     if lines[i].startswith("第"):
#         lines.insert(i, '[True, True, True, True, True, True]\n')
#         i = i+1
#     i = i + 1
# f.close()

## creating a unique code for each Gua using binary code, code will be in range 0 - 63 included.
# lines = f.readlines()
# for i in range(len(lines)):
#     if lines[i].startswith('['):
#         s = lines[i][1:-2]
#         s = s.replace(' ', '')
#         lst = s.split(',')
#         num = convert_to_num(lst)
#         lines[i] = str(num) + '\n'
# f.close()

## sort Gua by binary code
# lines = f.readlines()
# gua = {}
# gua[63] = ''
# s = ''
# code = 63
# for i in range(1, len(lines)):
#     if lines[i][:-1].isnumeric():
#         gua[code] = s
#         s = ''
#         code = int(lines[i])
#     else:
#         s = s + lines[i]
# gua[code] = s +'\n'
#
# lines = []
# for i in range(0,64):
#     lines.append(gua[i])
#     print(lines[i])


## find any lines that is not in the format, there are some 【白话】 that does not have 【】
# lines = f.readlines()
# for i in range(len(lines)):
#     if lines[i].startswith("白"):
#         print(str(i) + "     " + lines[i])

# write to file
# f = open(file, 'w', encoding='utf8')
# f.writelines(lines)
# f.close()





########################################################################################################################
