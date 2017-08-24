#!/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/8/16 21:11"


import pickle
import time

class Teacher():
    def __init__(self, name, sex, age, password, asset, teach_courses, evaluate_info):
        self.name = name
        self.sex = sex
        self.age = age
        self.password = password
        self.asset = asset
        self.teach_courses = teach_courses
        self.evaluate_info = evaluate_info


with open('teacher_A_teachinfo.txt', mode='rb') as f_r:
    content = pickle.load(f_r)
    print(content.name)
    print(content.sex)
    print(content.age)
    print(content.password)
    print(content.asset)
    print(content.teach_courses)
    print(content.evaluate_info)



# class Student():
#     def __init__(self, name, sex, age, password, courses_list, learn_record):
#             self.name = name
#             self.sex = sex
#             self.age = age
#             self.password = password
#             self.courses_list = courses_list
#             self.learn_record = learn_record
#
#
# with open('stu_A_stuinfo.txt', mode='rb') as f_r:
#     content = pickle.load(f_r)
#     print(content.name)
#     print(content.sex)
#     print(content.age)
#     print(content.password)
#     print(content.courses_list)
#     print(content.learn_record)

# content.courses_list = ['java','python']
#
# with open('yang_stuinfo.txt', mode='wb') as f_w:
#     pickle.dump(content,f_w)

# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#
# with open('courses_info.txt', mode='rb') as f:
#     content = pickle.load(f)
#     print(content)







