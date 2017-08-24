#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/8/3 16:35"

# d = {'a': 1, 'b': 2, 'c': [1, 2, 3]}
# with open('cs.txt', mode='wb') as f:
#     pickle.dump(d, f)
#
# with open('cs.txt', mode='rb') as f:
#     dict = pickle.load(f)
#
# print(dict)

# with open('teacher1_teachinfo.txt', mode='rb') as f:
#     dict = pickle.load(f)
# print(dict)

# with open('stu001_stuinfo.txt', mode='rb') as f:
#     dict = pickle.load(f)
# print(dict)

# 课程名称、上课时间、课时费、关联老师、---课程内容

# courses_dict = {'python全栈': ['teacher_001', '19800', '1、python基础，2、python进阶，3、python高级'],
#                 'python自动化': ['teacher_002', '18800', '1、python基础，2、linux基础，3、python高级，4、linux高级'],
#                 }
# print('当前课程有：')
# for k, v in courses_dict.items():
#     print(str(k) + ': ' + '课程教师：' + str(v[0]) + '\n\t\t\t课程费用：' + str(v[1]) + '\n\t\t\t课程内容：' + str(v[2]))


# with open('courses_info.txt', mode='rb') as f:
#     d = pickle.load(f)
#     print(d)
#
# print(">>>"*10)
#
# d={}
# with open('courses_info.txt', mode='wb') as f:
#     d['ruby'] = {'Elijah','15800','1、Ruby入门，2、Ruby高级'}
#     pickle.dump(d,f)
#     print(d)
#
# print("***"*10)
#
# with open('courses_info.txt', mode='rb') as f:
#     try:
#         d = pickle.load(f)
#     except Exception:
#         d={}
# print(d)

# with open('stu003_stuinfo.txt', mode='rb') as f:
#     d = pickle.load(f)
#     print(d)
#     print(type(d))

# with open('teacher1_teachinfo.txt', mode='rb') as f:
#     d = pickle.load(f)
#     print(d)
#     print(type(d))

# with open('courses_info.txt', mode='rb') as f_r:
#     courses_list = pickle.load(f_r)
#     print(courses_list)

# mapping_dict = {}
# for root, dirs, files in os.walk('./'):
#     # print(root) #当前目录路径
#     # print(dirs) #当前路径下所有子目录
#     # print(files) #当前路径下所有非目录子文件
#     # print(type(files))
#     count = 0
#     for i in files:
#         if 'stuinfo.txt' in i:
#             count += 1
#             mapping_dict[count] = i.split('_stuinfo.txt')[0]
#             print(count, i.split('_stuinfo.txt')[0])
# print(mapping_dict[2])

import os
import pickle


class Student():
    def __init__(self, name, sex, age, ):
        self.name = name
        self.sex = sex
        self.age = age

    def tell(self):
        print(self.name + '的tell方法执行！')


def write(name, obj):
    file_name = name + '_test.txt'
    with open(file_name, mode='wb') as f:
        pickle.dump(obj, f)


def read(name):
    file_name = name + '_test.txt'
    with open(file_name, mode='rb') as f_r:
        obj = pickle.load(f_r)
        return obj


# s1 = Student('张三','male','28')
# s1.write()
# print(s1.read().name)

def main():
    role = input('请选择角色:\n>>>').strip()
    if role == 's':
        is_exist = input('是否存在用户(y/n)?\n>>>').strip()
        if is_exist.lower() == 'n':
            name = input('请输入学生的姓名：\n').strip()
            sex = input('请输入学生的性别：\n').strip()
            age = input('请输入学生的年龄：\n').strip()
            password = input('请输入学生的密码：\n').strip()
            courses_list = input('请输入学生的课程列表(用顿号、隔开)：\n>>>').strip().split('、')
            learn_record = {}
            while True:
                learn_record_name = input('添加上课记录：\n请输入学生所上的课程名：\n>>>').strip()
                learn_record_time = input('请输入学生上课的时间：\n>>>').strip()
                learn_record_teacher = input('请输入学生上课的授课教师：\n>>>').strip()
                is_continue = input('是否继续添加上课记录(y/n)？\n>>>').strip()
                if is_continue.lower() == 'y':
                    learn_record[learn_record_name.ljust(10)] = [learn_record_time, learn_record_teacher]
                    continue
                elif is_continue.lower() == 'n':
                    learn_record[learn_record_name.ljust(10)] = [learn_record_time, learn_record_teacher]
                    break
                else:
                    print('对不起！输入有误，请重新输入！')
            s1 = Student(name, sex, age, password, courses_list, learn_record)
            write(name, 'stuinfo', s1)
            print('用户' + name + '创建成功！')
        elif is_exist.lower() == 'y':
            name = input('请输入学生的姓名：\n').strip()
            for root, dirs, files in os.walk('./'):
                for i in files:
                    if (name + '_stuinfo.txt') in i:
                        obj_stu = read(name, 'stuinfo')
                        print('当前用户的姓名为：' + obj_stu.name)
                        obj_stu.modify_stuinfo()
                        # obj_stu.search_courses()
                        # obj_stu.search_learnrecord()
                        write(name, 'stuinfo', obj_stu)
    else:
        print('有错误！')


main()
