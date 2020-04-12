import sys
import re

path = sys.argv[1]

def count_setting(pattern, num_split):
    file = open(path)
    lines = file.readlines()

    count_vsys = 0
    count_seting = 0
    vsys_pre = 'dumy'
    setting_pre = 'dumy'
    list_count = [997]

    i = 0

    for line in lines:
        # i += 1    #debug
        if re.match('^\n', line):   #改行の行の場合処理しない
            # print('null') #debug
            pass
        elif re.match('set vsys vsys.+', line):
            result = re.match('set vsys vsys.+', line)
            vsys = result.group(0).split()
            vsys = vsys[2]
            if (vsys == vsys_pre):                
                if re.match(pattern, line):
                    result = re.match(pattern, line)    #patternで定義した正規表現でマッチ
                    setting = result.group(0).split()   #スペースで分割
                    setting = setting[num_split]    #設定名称部分だけ抜き出し
                    if (setting == setting_pre):    #前回の設定名称と同じ場合カウントしない
                        setting_pre = setting
                        vsys_pre = vsys
                        #print('...',setting)   #debug
                    elif (setting != setting_pre):  #前回の設定名称と違う場合、カウントする
                        setting_pre = setting
                        count_seting += 1
                        vsys_pre = vsys
                        #print(count_seting,setting)    #debug
                        pass
                else:
                    vsys_pre = vsys
                    pass
            elif (vsys != vsys_pre):
                list_count.append(count_seting)
                count_seting = 0
                vsys_pre = vsys
                # print(vsys_pre, len(list_count))  #debug
                pass
        elif re.match('vsys', vsys_pre):    #vsys設定の読み込みで最後の行が終わったときに最後のカウント数をappendする
            vsys_pre = 'end'
            list_count.append(count_seting)
            # print(i,line,'end')   #debug
            pass 
        pass
    del list_count[1]    
    return(list_count)
    pass


def total(list_count):
    total_count = 0
    for i in range(1,len(list_count)):
        total_count+=list_count[i]
        # print(i,total_count)      #debug
    return(total_count)
    pass
    




filename = sys.argv[1].split("/")
print('**%s**' % filename[len(filename)-1])


# service
print('-servise')
list_count = count_setting(pattern = '.+vsys[1-9]+ service .+', num_split = 4)  #vsys毎のservie設定数
#print(" -count per vsys:\n",list_count)

total_count = total(list_count)
print(" -totalcount:",total_count)

#security rule
print('-security rule')
list_count = count_setting(pattern = '.+security rules .+', num_split = 6)  #vsys毎のsecurity rules設定数
#print(" -count per vsys:\n",list_count)

total_count = total(list_count)
print(" -totalcount:",total_count)    

#url
print('-url-filtering')
list_count = count_setting(pattern = '.+vsys[1-9]+ profiles url-filtering .+', num_split = 5)  #vsys毎のurl-filtering設定数
#print(" -count per vsys:\n",list_count)

total_count = total(list_count)
print(" -totalcount:",total_count)    

