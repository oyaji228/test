# 読込むファイルのパスを宣言する
import sys
import re

path = sys.argv[1]

# def count():
#     count = 0
#     count_split = 0
#     split_pre = 'dumy'


#     num_split_vsys = 2
#     file = open(path)
#     lines = file.readlines()

#     for line in lines:
#         if re.match('set vsys vsys.+', line):
#             result = re.match('set vsys vsys.+', line)
#             split = result.group(0).split()
#             count_split = splitcount(pattern = '.+vsys[1-9]+ service .+', num_split = 4)
#             print(count_split)
#             if (split[2] == split_pre): #前回のmatch結果と同じ場合カウントしない
#                 split_pre = split[2]
#                 print('...',split[2])
#             else:
#                 split_pre = split[2]
#                 count += 1
#                 print(count,split[2])
#                 pass
#             pass
#     return(count)
#     file.close()

#     return(count)
#     pass

def splitcount(pattern='', num_split=0):
    file = open(path)
    lines = file.readlines()

    count = 0
    split_pre = 'dumy'


    for line in lines:
        if re.match(pattern, line):
            result = re.match(pattern, line) #patternで定義した正規表現でマッチ
            split = result.group(0).split() #スペースで分割
            split = split[num_split]
            #print(result.group(0))
            if (split == split_pre): #前回のmatch結果と同じ場合カウントしない
                split_pre = split
                #print('...',split)
            else:
                split_pre = split
                count += 1
                #print(count,split) #splitで区切ったうち'name'のみ表示
                pass
            pass
    file.close()

    return(count)
    pass



def vsys_count():
    file = open(path)
    lines = file.readlines()
    #pattern = '.+vsys.+User[0-9]+-vwire'
    pattern = 'set network virtual-wire (V|U).+'
    num_vsys = 0
    for line in lines:
        if re.match(pattern, line):
            #print(line, end="")
            num_vsys+=1
            pass
        pass
    num_vsys = num_vsys / 2 
    print('vsys: %d' % num_vsys)
    pass


def print_res(match_num=0, count=0):
    if match_num == 1: #servie
        match_name = "service"
        maxvalue = 10000
        cal_pre = count / maxvalue
        cal = '{:.0%}'.format(cal_pre)
        print('%s: %d (resource utilization: %s @max:%d)' % (match_name, count, cal, maxvalue)) 
        pass
    elif match_num == 2: #security rules
        match_name = "security rules"
        maxvalue = 20000
        cal_pre = count / maxvalue
        cal = '{:.0%}'.format(cal_pre)
        print('%s: %d (resource utilization: %s @max:%d)' % (match_name, count, cal, maxvalue)) 
        pass
    elif match_num == 3: #url-filtering profile
        match_name = "url-filtering profile"
        maxvalue = 750
        cal_pre = count / maxvalue
        cal = '{:.0%}'.format(cal_pre)
        print('%s: %d (resource utilization: %s @max:%d)' % (match_name, count, cal, maxvalue)) 
        pass
    pass


split_filename = sys.argv[1].split("/")
print('[%s]' % split_filename[1])

# count = count()

vsys_count()

# match_num = 1
# count = splitcount(pattern = '.+vsys[1-9]+ service .+', num_split = 4)
# print_res(match_num, count)

match_num = 2
count = splitcount(pattern = '.+security rules .+', num_split = 6)
print_res(match_num, count)

# match_num = 3
# count = splitcount(pattern = '.+vsys[1-9]+ profiles url-filtering .+', num_split = 5)
# print_res(match_num, count)

