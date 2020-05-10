# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:01:12 2020

@author: HaoranLi
"""

import School

#实例化数据库课程
dta=School.Course('001','数据库技术与应用','李秀',3,50)
#读取学生列表并让其选课
students=[]
k=0
filename='学生列表.txt'
with open(filename) as file_object:
    for line in file_object:
        s=line.split()
        sname=s[0]
        sno=s[1]
        students.append(School.Student(sname,sno))
        students[k].select_course(dta)
        k+=1
#抽签
dta.draw_lots()
#输出课程内和候选学生名单
print("课程内学生名单为：")
for i in range(len(dta.selectionStudents)):
    print(dta.selectionStudents[i].ID)
print("队列学生名单为：")
for j in range(len(dta.waitingStudents)):
    print(dta.waitingStudents[j].ID)
print("课程内人数"+str(len(dta.selectionStudents)))
print("队列人数"+str(len(dta.waitingStudents)))
