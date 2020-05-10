Database_Coursework
===================
This repository contains courseworks for Database Technology and Application(2020Spring) in Tsinghua University.

GPATool
-------------------
### 程序的输入:
    一份20行的成绩单字符串，每行记录有三条信息：课程名、学分和绩点。
### 程序分为以下几个部分:
* 数据提取与保存
   * 首先接受输入，使用split("\n")将其按行分割；
   * 然后使用split()按照空格分割，并将其存储到字典的列表courseList中，每个字典有三个键值对，分别对应课程名、学分和绩点。
* 功能实现<br>
    编写三个功能函数和一个辅助函数实现：
   * 判断浮点数:isfloat(aString)
   * 计算GPA：calGPA(courseList)
   * 计算获得总学分：calCredit(courseList)
   * 获取绩点高于GPA的课程:goodCourse(courseList)
### 程序的输出:
    0/退出 1/GPA 2/获得总学分 3/绩点高于GPA的课程
    
选课系统
-------------------
    分为Main.py和School.py两个模块
### School.py:
    实现学生类Student和课程类Course
* Student类
   * 包括属性name和ID，以及用来记录预选课信息、正选课信息和队列课信息的三个列表preselectionCourses、selectionCourses和waitingCourses
   * 选课函数select_course()，当学生选课时1.将学生与选课列表加上该课程 2.将该课程预选学生列表加上当前学生
* Course类
   * 包含属性cno,cname,teacher,credit,capacity，以及用来记录预选学生、正选学生和队列学生的三个列表preselectionStudents、selectionStudents和waitingStudents
   * 抽签函数draw_lots()，当抽签时使用random.shuffle(list)将预选学生列表随机打乱，然后将capacity内的学生放入正选列表，预选课信息删除，加入正选课，capacity之外的学生放入队列列表，预选课信息删除，加入队列课信息。最后将预选学生列表清空。

### Main.py:
* 实例化数据库课程
* 从学生列表.txt中读取学生信息并创建students[]列表用来存放学生对象，每个学生均预选数据库课程
* 抽签
* 输出结果

