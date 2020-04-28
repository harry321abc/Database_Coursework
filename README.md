Database_Coursework
===================
This repository contains courseworks for Database Technology and Application(2020Spring) in Tsinghua University.

GPATool
-------------------
#程序的输入:
    一份20行的成绩单字符串，每行记录有三条信息：课程名、学分和绩点。<br>
#程序分为以下几个部分:
* 数据提取与保存
   * 首先接受输入，使用split("\n")将其按行分割；
   * 然后使用split()按照空格分割，并将其存储到字典的列表courseList中，每个字典有三个键值对，分别对应课程名、学分和绩点。
* 功能实现
    编写三个功能函数和一个辅助函数实现：
   * 判断浮点数:isfloat(aString)
   * 计算GPA：calGPA(courseList)
   * 计算获得总学分：calCredit(courseList)
   * 获取绩点高于GPA的课程:goodCourse(courseList)
#程序的输出
    0/退出 1/GPA 2/获得总学分 3/绩点高于GPA的课程


