#!/usr/bin/python
# -*- coding:utf8 -*-
f = open('score.txt')
f2 = open('newscore.txt','a')
lines = f.readlines()        #readlines把每行分成了一个list中的4个项目,每个项目是一个字符串
print lines
for line in lines:           #变量line相当于i；for循环会遍历lines这个list中的每一项（用逗号分开），这里有4项
    data = line.split()      #split正好又对字符串操作；4个字符串又分别按空格被切割成4个list，
    sum = 0
    for score in data[1:]:
        sum += int(score)    #字符串格式要转化为int,对score加，而不是输入data[1:]这个list
    result = '%s\t:%d\n' %(data[0] , sum) #变量result又变回了字符串；\n不要忘
    print result
    f2.write(result)                      #总结一下数据类型的变化：字符串→list→list中字符串→每个字符串变成1个list
f.close()
f2.close()