# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:07:32 2020

@author: HaoranLi
"""
import random

class Student():
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID
        self.preselectionCourses=[]#预选课列表
        self.selectionCourses=[]#正选课列表
        self.waitingCourses=[]#队列课列表
    def select_course(self,course):
        self.preselectionCourses.append(course)
        course.preselectionStudents.append(self)
        
        
class Course():
    def __init__(self,cno,cname,teacher,credit,capacity):
        self.cno=cno
        self.cname=cname
        self.teacher=teacher
        self.credit=credit
        self.capacity=capacity
        self.preselectionStudents=[]#预选学生列表
        self.selectionStudents=[]#正选学生列表
        self.waitingStudents=[]#队列学生列表
    def draw_lots(self):
        random.shuffle(self.preselectionStudents)
        for i in range(self.capacity):
            self.preselectionStudents[i].preselectionCourses.pop()
            self.preselectionStudents[i].selectionCourses.append(self)
            self.selectionStudents.append(self.preselectionStudents[i])
        for j in range(len(self.preselectionStudents)-self.capacity):
            self.preselectionStudents[j+self.capacity].preselectionCourses.pop()
            self.preselectionStudents[j+self.capacity].waitingCourses.append(self)
            self.waitingStudents.append(self.preselectionStudents[j+self.capacity])
        self.preselectionStudents.clear
        
        
            
        
        
        
        
        
    