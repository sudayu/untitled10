

import re
import codecs
import re
#读取txt中的内容
with open(r'c:\file1\BB13_UNION_20190818.txt',encoding="utf-8") as f:
    mylist = f.readlines()
    #List列表形式
    #print(mylist)
    list1= []
    list2=[]
    for content in mylist:
        #content.strip()去掉\n换行符
        a = content.strip().split("|")
        b = a[0:16]  # 这是选取需要读取的位数 0:1表示第一列，1:2表示第2列
        list1.append(b)  # 将其添加在列表之中
    #print(list1[0])
    #列表名称，需要保留原有，字符串形式    发给
    list3 = '|'.join( list1[0])
    print(list3)
    f.close()
    #从第二行进行遍历、
    for i in list1[1:]:
        # 身份证翻转后，前6位加密--也就是正常身份证后6位加密
        # 列表转字符串
        UNIONORGKEY = ''.join(i[0])
        n=6
        ch = '*'
        str1=UNIONORGKEY[::-1]
        str2 = n*ch+str1[6:]
        #str1 = ''.join(str) #字符串每隔一个字母就加一个*，后面在拼接一个
        #print(str2)
        #姓名中，名是*
        UNION_NAME = ''.join(i[5])
        #print(UNION_NAME)
        if len(UNION_NAME)>2 :
            ch ='**'
            u=UNION_NAME[0:1]+''.join(ch)
        else:
            u = UNION_NAME[0:1] + ''.join(ch)
        #print(u)
        #手机号码
        m=4
        c='*'
        TELPHONE=''.join(i[0])
        T=TELPHONE[0:3]+m*c+TELPHONE[7:]
        #print(T)
        #字符串转列表 str2.split('|')
        S=str2.split('|')+u.split('|')+T.split('|')+i[4:]
        #生成字符串
        #S1=''.join(str2),+''.join(u)+''.join(T)
        #生成原txt文件形式，以|分割开
        for x in S:
            print(x,end='|')
        #print(S)
        #将多行list合并成一个list
        list2.append(S)
        f.close()
        # 列表S写入1.txt文件
        #字符串写入用write,列表写入用writelines
        with open(r"c:/file1/1.txt","w",encoding="utf-8") as fw:
            #写入列名
            fw.write(list3+'\n')
            for j in list2:
                fw.write(('|'.join(map(str, j))+'\n'))
        fw.close()





