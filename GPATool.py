# -*- coding: utf-8 -*-
"""
Harry

GPA综合版（作业）
"""
def isfloat(aString):
    try:
        float(aString)
        return True
    except:
        return False

def calGPA(courseList):
    creditSum = 0 #总学分和
    gradePoint = 0 #总学分绩点乘积和
    for course in courseList:
        a=course['学分']
        b=course['绩点']
        #如果绩点不是P\F\W等字母，参与计算GPA
        if isfloat(b):
            creditSum = creditSum + int(a) #计算学分和
            gradePoint = gradePoint + int(a) * float(b) #计算学分绩点乘积和
    GPA = gradePoint/creditSum
    return GPA

def calCredit(courseList):
    creditSum=0
    for course in courseList:
        #若绩点是数字或者P，则加入总学分
        if (isfloat(course['绩点'])) or (course['绩点']=="P"):
            creditSum+=int(course['学分'])
    return creditSum

def goodCourse(courseList):
    GPA=calGPA(courseList)
    for course in courseList:
        #若绩点是数字，则参与比较
        if isfloat(course['绩点']):
            #若绩点大于GPA，则输出对应的课程名
            if float(course['绩点'])>GPA:
                print("\n"+course['课程名'])
    return

if __name__=='__main__':
    records=input("请输入成绩单：")#输入整张成绩单
    recordList=records.split("\n")#将成绩单分割成每一条记录
    courseList=[]
    #把每一条记录（列表）转化成字典
    for i in range(20):
        record=recordList[i].split()
        courseName=record[0]
        credit=record[1]
        gradePoint=record[2]
        new_course={'课程名':courseName,'学分':credit,'绩点':gradePoint}
        courseList.append(new_course)
    #让用户选择不同的操作
    option=int(input("输入以下命令执行不同操作：\n0、退出 \n1、查询GPA\n2、查询总学分\n3、查询绩点高于GPA的科目"))
    while (option!=0):
        #查询GPA
        if option==1:
            print(calGPA(courseList))
            option=int(input("输入以下命令执行不同操作：\n0、退出 \n1、查询GPA\n2、查询总学分\n3、查询绩点高于GPA的科目"))
        #查询总学分
        elif option==2:
            print(calCredit(courseList))
            option=int(input("输入以下命令执行不同操作：\n0、退出 \n1、查询GPA\n2、查询总学分\n3、查询绩点高于GPA的科目"))
        #查询绩点高于GPA的科目
        elif option==3:
            goodCourse(courseList)
            option=int(input("输入以下命令执行不同操作：\n0、退出 \n1、查询GPA\n2、查询总学分\n3、查询绩点高于GPA的科目"))
    
    