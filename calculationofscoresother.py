#!/usr/bin/python
# -*- coding:utf8 -*-
f = file('scores.txt')
lines = f.readlines()
#print lines
f.close()

results = []                     #创建一个list，使得每得到一个学生的总成绩后，就把它添入其中。

for line in lines:
   #print line
   data = line.split()
   #print data

   sum = 0                #对于每一条数据，都新建一个字符串，把学生的名字和算好的总成绩保存进去。最后再把这些字符串一起保存到文件中
   for score in data[1:]:
       sum += int(score)
   result = '%s \t: %d\n' % (data[0], sum)
   #print result

   results.append(result)       #放在循环内部，得到一个学生的总成绩后，把它添加到list中。

#print results
output = file('result.txt', 'w')
output.writelines(results)      #全部成绩处理完毕后，保存results中内容至文件。因为results是一个字符串组成的list，这里我们直接用writelines
output.close()