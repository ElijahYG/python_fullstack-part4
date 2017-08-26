#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "Elijah"
__date__ = "2017/8/1 21:37"

import os
import pickle
import time


def write(name, role, obj):
    file_name = name + '_' + role + '.txt'
    with open(file_name, mode='wb') as f:
        pickle.dump(obj, f)


def read(name, role):
    file_name = name + '_' + role + '.txt'
    with open(file_name, mode='rb') as f_r:
        obj = pickle.load(f_r)
        return obj


class Student():
    def __init__(self, name, sex, age, password, courses_list, learn_record):
        self.name = name
        self.sex = sex
        self.age = age
        self.password = password
        self.courses_list = courses_list
        self.learn_record = learn_record

    def modify_stuinfo(self):
        while True:
            attr_fields = '''
当前学生%s信息为：
    1、性别 : %s
    2、年龄 : %s
    3、密码 : %s
    4、课程列表 : %s
    5、上课记录 : %s
            ''' % (self.name, self.sex, self.age, self.password, self.courses_list, self.learn_record)
            print(attr_fields)
            modi_attr = input('请输入您想要修改的字段的对应编号(或输入Q退出)：\n>>>').strip()
            if modi_attr == '1':
                changed_attr = input('当前字段值为: ' + self.sex + ' 请输入您要变更的字段内容：\n>>>').strip()
                self.sex = changed_attr
            elif modi_attr == '2':
                changed_attr = input('当前字段值为: ' + self.age + ' 请输入您要变更的字段内容：\n>>>').strip()
                self.age = changed_attr
            elif modi_attr == '3':
                changed_attr = input('当前字段值为: ' + self.password + ' 请输入您要变更的字段内容：\n>>>').strip()
                self.password = changed_attr
            elif modi_attr == '4':
                changed_attr = input(
                    '当前课程列表为: ' + str(self.courses_list) + ' 请输入您要变更的课程列表(用顿号、隔开)：\n>>>').strip().split('、')
                self.courses_list = changed_attr
            elif modi_attr == '5':
                changed_attr_name = input('当前上课记录为: ' + str(self.learn_record) + '\n请输入您要变更的上课记录-课程名：\n>>>').strip()
                changed_attr_time = input('请输入您要变更的上课记录-上课时间：\n>>>').strip()
                changed_attr_teacher = input('请输入您要变更的上课记录-授课教师：\n>>>').strip()
                self.learn_record[changed_attr_name.ljust(10)] = [changed_attr_time, changed_attr_teacher]
            elif modi_attr.lower() == 'q':
                break
            else:
                print('对不起！您输入的编号有错误，请重新输入！')
                continue
            write(self.name, 'stuinfo', self)
            print('修改保存成功！当前学生：' + self.name + '的信息为：\n性别：' + self.sex + '\n年龄：' + self.age +
                  '\n密码：' + self.password + '\n所选课程：' + str(self.courses_list) + '\n学习记录：' + str(self.learn_record))

    def learn_courses(self):
        while True:
            coursenum_dict = {}
            student_file = self.name + "_stuinfo.txt"
            with open(student_file, mode='rb') as f_sr:
                student_info = pickle.load(f_sr)
            for i, k in enumerate(student_info.courses_list):
                coursenum_dict[i + 1] = k
                print(str(i + 1) + ':', k)
            select_num = input('请选择要学习的课程对应编号(或输入Q退出):\n>>>').strip()
            if select_num.lower() == 'q':
                break
            elif int(select_num):
                with open('courses_info.txt', mode='rb') as f_cr:
                    courses_dict = pickle.load(f_cr)
                try:
                    courses_dict[coursenum_dict[int(select_num)]][3]
                except Exception:
                    print('对不起，您输入的课程编号有误，请重新输入！')
                    continue
            else:
                print('对不起，您输入的课程编号有误！')
                continue
            print('学习内容为：')
            print(courses_dict[coursenum_dict[int(select_num)]][3] + '\n课程结束！')
            teacher = courses_dict[coursenum_dict[int(select_num)]][0]
            teacher_file = teacher + '_teachinfo.txt'
            self.learn_record[coursenum_dict[int(select_num)].ljust(10)] = \
                [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), teacher]
            with open(teacher_file, mode='rb') as f_tr:
                teacher_info = pickle.load(f_tr)
            while True:
                userinput_evaluate_info_content = input('\n评价内容(请输入对应评价的数字编号)：\n1、很好\n2、一般\n3、差\n>>>').strip()
                uinput_eval_info_cont_val = {'1': '很好', '2': '一般', '3': '差', }
                if (userinput_evaluate_info_content == '1') or (userinput_evaluate_info_content == '2'):
                    teacher_info.asset = str(int(teacher_info.asset) + 100)
                    break
                elif userinput_evaluate_info_content == '3':
                    teacher_info.asset = str(int(teacher_info.asset) - 50)
                    break
                else:
                    print('对不起，您输入的评价内容编号有误，请重新输入！')
                    continue
            teacher_info.evaluate_info[self.name] = uinput_eval_info_cont_val[userinput_evaluate_info_content]
            with open(teacher_file, mode='wb') as f_tw:
                pickle.dump(teacher_info, f_tw)
            with open(student_file, mode='wb') as f_sw:
                pickle.dump(self, f_sw)
            print('欢迎再次参加本课程，再见！')

    def search_courses(self):
        while True:
            courses_list = self.courses_list
            print('当前学生' + self.name + '所选课程为：')
            for count, i in enumerate(courses_list):
                print('\t' + str(count + 1) + '\t' + i)
            is_exit = input('是否退出(y/n)?\n>>>').strip()
            if is_exit.lower() == 'y':
                break
            elif is_exit.lower() == 'n':
                continue

    def search_learnrecord(self):
        learn_record = self.learn_record
        print('学生' + self.name + '上课记录为：')
        print('\t课程名称\t上课时间\t\t\t授课教师')
        for k, v in learn_record.items():
            print('\t' + k + '\t' + v[0] + '\t' + v[1])

    def select_course(self):
        flag1 = False
        flag2 = False
        while True:
            courses_all = []
            student_course = {}
            available_course = {}
            print('欢迎来到自选课程功能！当前学生' + self.name + '已选课程为：\n')
            for n, i in enumerate(self.courses_list):
                print(str(n + 1) + '、' + i)
            stu_choice = input('\n请选择操作编号(或输入Q退出)：\n1、\033[1;32m添加\033[0m课程\n2、\033[1;31m删除\033[0m课程\n>>>').strip()
            if stu_choice.lower() == '1':
                print('当前所有课程信息为：')
                with open('courses_info.txt', mode='rb') as f_r:
                    try:
                        courses_dict = pickle.load(f_r)
                    except Exception:
                        courses_dict = {}
                for k, v in courses_dict.items():
                    courses_all.append(k)
                    print(str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) + '\n\t\t课程费用：'
                          + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
                while not flag1:
                    print('\n您还可以选择添加以下课程：')
                    for n, i in enumerate(list(set(courses_all).difference(set(self.courses_list)))):
                        available_course[n + 1] = i
                        print(str(n + 1) + '、' + i)
                    choice_course = input('请选择要添加的课程所对应的的编号(或输入Q退出)：\n>>>').strip()
                    if choice_course.lower() == 'q':
                        pass
                    else:
                        if isinstance(int(choice_course), int):
                            self.courses_list.append(available_course[int(choice_course)])
                            print('学生' + self.name + '课程添加完成！当前所选课程为：\n')
                            for n, i in enumerate(self.courses_list):
                                print(str(n + 1) + '、' + i)
                        else:
                            print('对不起，请输入课程所对应的的编号')
                            continue
                    is_continue = input('是否继续操作(y/n)?\n>>>').strip()
                    if is_continue.lower() == 'y':
                        continue
                    elif is_continue.lower() == 'n':
                        break
                    else:
                        print('对不起，您的输入有误！\n')
                        break
            elif stu_choice.lower() == '2':
                while not flag2:
                    for n, i in enumerate(self.courses_list):
                        student_course[n + 1] = i
                        print(str(n + 1) + '、' + i)
                    if self.courses_list:
                        delete_num = input('请选择要\033[1;31m删除\033[0m课程的编号：\n').strip()
                        self.courses_list.remove(student_course[int(delete_num)])
                        print('课程' + student_course[int(delete_num)] + '删除成功！当前学生' + self.name + '所选课程为：\n')
                        for n, i in enumerate(self.courses_list):
                            print(str(n + 1) + '、' + i)
                    elif not self.courses_list:
                        print('对不起，当前学生没有已选课程，请添加课程后使用此删除功能！\n')
                        break
                    is_continue = input('是否继续操作(y/n)?\n>>>').strip()
                    if is_continue.lower() == 'y':
                        continue
                    elif is_continue.lower() == 'n':
                        break
                    else:
                        print('对不起，您的输入有误！\n')
                        break
            elif stu_choice.lower() == 'q':
                print('谢谢使用学生自选课程功能，再见！\n')
                break
            else:
                print('对不起，您的输入有误！')
                continue


class Teacher():
    def __init__(self, name, sex, age, password, asset, teach_courses, evaluate_info):
        self.name = name
        self.sex = sex
        self.age = age
        self.password = password
        self.asset = asset
        self.teach_courses = teach_courses
        self.evaluate_info = evaluate_info

    def modify_teachinfo(self):
        mapping_dict = {}
        evaluate_info = {}
        while True:
            attr_fields = '''
当前教师%s信息为：
    1、性别 : %s
    2、年龄 : %s
    3、密码 : %s
    4、资产 : %s
    5、教授课程 : %s
    6、评价信息 : %s
            ''' % (self.name, self.sex, self.age, self.password, self.asset, self.teach_courses, self.evaluate_info)
            print(attr_fields)
            modi_attr = input('请输入您想要修改的字段的对应编号(或输入Q退出)：\n>>>').strip()
            if modi_attr == '1':
                changed_attr = input('当前字段值为: ' + self.sex + ' 请输入您要变更的字段内容：\n>>>').strip()
                self.sex = changed_attr
            elif modi_attr == '2':
                changed_attr = input('当前字段值为: ' + self.age + ' 请输入您要变更的字段内容：\n>>>').strip()
                self.age = changed_attr
            elif modi_attr == '3':
                changed_attr = input('当前字段值为: ' + self.password + ' 请输入您要变更的字段内容：\n>>>').strip()
                self.password = changed_attr
            elif modi_attr == '4':
                changed_attr = input('当前字段值为: ' + self.asset + ' 请输入您要变更的字段内容：\n>>>').strip()
                self.password = changed_attr
            elif modi_attr == '5':
                changed_attr = input(
                    '当前教授课程为: ' + str(self.teach_courses) + ' 请输入您要变更的教授课程(用顿号、隔开)：\n>>>').strip().split('、')
                self.teach_courses = changed_attr
            elif modi_attr == '6':
                while True:
                    uinput_eval_info_cont_val = {'1': '很好', '2': '一般', '3': '差', }
                    print('当前所有学生账号如下：')
                    for root, dirs, files in os.walk('./'):
                        count = 0
                        for i in files:
                            if 'stuinfo.txt' in i:
                                count += 1
                                mapping_dict[count] = i.split('_stuinfo.txt')[0]
                                print(count, i.split('_stuinfo.txt')[0])
                    student_num = input('修改评价信息：\n请输入评价该教师的学生姓名对应的编号：\n>>>').strip()
                    evaluate_info_name = mapping_dict[int(student_num)]
                    try:
                        self.evaluate_info[evaluate_info_name]
                    except Exception:
                        print('对不起，该学生未对教师进行评价，请选择已存在的评价信息进行修改！')
                        continue
                    print(uinput_eval_info_cont_val)
                    evaluate_info_num = input('请输入该学生对此教师评价的对应编号：\n>>>').strip()
                    if 0 < int(evaluate_info_num) < 4:
                        evaluate_info_content = uinput_eval_info_cont_val[evaluate_info_num]
                    else:
                        print('对不起，您输入的编号有误！')
                        continue
                    is_continue = input('是否继续添加评价信息(y/n)？\n>>>').strip()
                    if is_continue.lower() == 'y':
                        evaluate_info[evaluate_info_name] = \
                            [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), evaluate_info_content]
                        continue
                    elif is_continue.lower() == 'n':
                        evaluate_info[evaluate_info_name] = \
                            [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), evaluate_info_content]
                        break
                    else:
                        print('对不起！输入有误，请重新输入！')
                        continue
            elif modi_attr.lower() == 'q':
                break
            else:
                print('对不起！您输入的编号有错误，请重新输入！')
                continue
            write(self.name, 'stuinfo', self)
            print('修改保存成功！当前教师：' + self.name + '的信息为：\n性别：' + self.sex + '\n年龄：' + self.age +
                  '\n密码：' + self.password + '\n资产：' + self.asset + '\n教授课程：' + str(self.teach_courses) +
                  '\n评价信息：' + str(self.evaluate_info))

    def search_teach(self):
        while True:
            courses_list = self.teach_courses
            print('当前教师' + self.name + '的教授课程为：')
            for count, i in enumerate(courses_list):
                print('\t' + str(count + 1) + '\t' + i)
            is_exit = input('是否退出(y/n)?\n>>>').strip()
            if is_exit.lower() == 'y':
                break
            elif is_exit.lower() == 'n':
                continue

    def search_evaluate(self):
        evaluate_info = self.evaluate_info
        print('教师' + self.name + '评价信息为：')
        print('\t学生姓名\t评价内容')
        for k, v in evaluate_info.items():
            print('\t' + k + '\t\t' + v)


class Admin():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def add_student(self):
        while True:
            courses_list = []
            learn_record = {}
            mapping_course = {}
            learn_record_teacher = ''
            print('欢迎来到创建学生账号功能，请依次输入用户名、性别、年龄、密码、课程列表与上课记录')
            name = input('请输入学生的姓名(或输入Q退出)：\n').strip()
            if name.lower() == 'q':
                break
            sex = input('请输入学生的性别(或输入Q退出)：\n').strip()
            if sex.lower() == 'q':
                break
            age = input('请输入学生的年龄(或输入Q退出)：\n').strip()
            if age.lower() == 'q':
                break
            password = input('请输入学生的密码(或输入Q退出)：\n').strip()
            if password.lower() == 'q':
                break
            while True:
                count = 0
                print('当前课程信息为：')
                with open('courses_info.txt', mode='rb') as f_r:
                    try:
                        courses_dict = pickle.load(f_r)
                    except Exception:
                        courses_dict = {}
                for k, v in courses_dict.items():
                    count += 1
                    mapping_course[count] = k
                    print(str(count) + '、' + str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) +
                          '\n\t\t课程费用：' + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
                choice_course = input('请选择学生的课程，输入对应编号(或输入Q退出)：\n>>>').strip()
                if choice_course.lower() == 'q':
                    break
                elif int(choice_course):
                    courses_list.append(mapping_course[int(choice_course)])
                else:
                    print('对不起，您的输入有误！')
                    continue
                is_add = input('课程添加成功！是否继续添加课程(y/n)?\n>>>').strip()
                if is_add.lower() == 'y':
                    continue
                elif is_add.lower() == 'n':
                    break
            while True:
                count = 0
                is_learn_record = input('是否添加上课记录(y/n)？').strip()
                if is_learn_record.lower() == 'y':
                    print('当前课程信息为：')
                    with open('courses_info.txt', mode='rb') as f_r:
                        try:
                            courses_dict = pickle.load(f_r)
                        except Exception:
                            courses_dict = {}
                    for k, v in courses_dict.items():
                        count += 1
                        mapping_course[count] = k
                        learn_record_teacher = str(v[0])
                        print(str(count) + '、' + str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) +
                              '\n\t\t课程费用：' + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
                    learn_record_num = input('添加上课记录：\n请输入学生所上的课程名对应的编号：\n>>>').strip()
                    learn_record_time = input('请输入学生上课的时间(例：2017-08-20 20:15)：\n>>>').strip()
                    learn_record_name = mapping_course[int(learn_record_num)]
                    learn_record[learn_record_name.ljust(10)] = [learn_record_time, learn_record_teacher]
                    is_continue = input('是否继续添加上课记录(y/n)？\n>>>').strip()
                    if is_continue.lower() == 'y':
                        continue
                    elif is_continue.lower() == 'n':
                        break
                    else:
                        print('对不起！输入有误，请重新输入！')
                elif is_learn_record.lower() == 'n':
                    break
            s1 = Student(name, sex, age, password, courses_list, learn_record)
            write(name, 'stuinfo', s1)
            print('用户' + name + '创建成功！')

    def delete_student(self):
        while True:
            print('当前所有学生账号如下：')
            count = 0
            mapping_dict = {}
            for root, dirs, files in os.walk('./'):
                for i in files:
                    if 'stuinfo.txt' in i:
                        count += 1
                        mapping_dict[count] = i.split('_stuinfo.txt')[0]
                        print(count, i.split('_stuinfo.txt')[0])
            delete_num = input('请输入您要\033[1;31m删除\033[0m学生账号前所对应的编号(或输入Q退出)：\n>>>').strip()
            if delete_num.lower() == 'q':
                break
            elif 0 < int(delete_num) <= count:
                print('您所选择的学生信息如下：')
                file_name = mapping_dict[int(delete_num)] + '_stuinfo.txt'
                with open(file_name, mode='rb') as f_r:
                    student_info = pickle.load(f_r)
                    print('\t\t学生姓名：' + str(student_info.name) + '\n\t\t性别：' + str(student_info.sex) +
                          '\n\t\t年龄：' + str(student_info.age) + '\n\t\t所选课程：' + str(student_info.courses_list) +
                          '\n\t\t上课记录：' + str(student_info.learn_record))
                is_true = input('\n是否确认要删除该学生账号(y/n)?\n>>>').strip()
                if is_true.lower() == 'y':
                    file_path = './' + file_name
                    os.remove(file_path)
                    is_continue = input('成功删除学生 ' + mapping_dict[int(delete_num)] + ' 的账号！是否继续删除(y/n)？').strip()
                    if is_continue.lower() == 'y':
                        continue
                    elif is_continue.lower() == 'n':
                        break
                    else:
                        print('对不起，你的输入有误，请重新输入！')
                        break
                else:
                    print('对不起输入有误！')
            else:
                print('对不起，你输入的编号有错误，请重新输入！')
                continue

    def modify_student(self):
        while True:
            flag = False
            mapping_dict = {}
            courses_num = 0
            courses_dict = {}
            changed_attr = []
            learn_record_dict = {}
            print('当前所有学生账号如下：')
            for root, dirs, files in os.walk('./'):
                count = 0
                for i in files:
                    if 'stuinfo.txt' in i:
                        count += 1
                        mapping_dict[count] = i.split('_stuinfo.txt')[0]
                        print(count, i.split('_stuinfo.txt')[0])
            modify_num = input('请输入您要修改学生账号前所对应的编号(或输入Q退出)：\n>>>').strip()
            if modify_num.lower() == 'q':
                break
            else:
                print('您所选择的学生信息如下：')
                file_name = mapping_dict[int(modify_num)] + '_stuinfo.txt'
                with open(file_name, mode='rb') as f_r:
                    student_info = pickle.load(f_r)
                while not flag:
                    attr_fields = '''
当前学生%s信息为：
    1、性别 : %s
    2、年龄 : %s
    3、密码 : %s
    4、课程列表 : %s
    5、上课记录 : %s
                    ''' % (
                        student_info.name, student_info.sex, student_info.age, student_info.password,
                        student_info.courses_list,
                        student_info.learn_record)
                    print(attr_fields)
                    modi_attr = input('请输入您想要修改的字段的对应编号(或输入Q退出)：\n>>>').strip()
                    if modi_attr == '1':
                        changed_attr = input('当前字段值为: ' + student_info.sex + ' 请输入您要变更的字段内容：\n>>>').strip()
                        student_info.sex = changed_attr
                    elif modi_attr == '2':
                        changed_attr = input('当前字段值为: ' + student_info.age + ' 请输入您要变更的字段内容：\n>>>').strip()
                        student_info.age = changed_attr
                    elif modi_attr == '3':
                        changed_attr = input('当前字段值为: ' + student_info.password + ' 请输入您要变更的字段内容：\n>>>').strip()
                        student_info.password = changed_attr
                    elif modi_attr == '4':
                        with open('courses_info.txt', mode='rb') as f_r:
                            courses_dict = pickle.load(f_r)
                        print('系统所有课程如下：')
                        for k, v in courses_dict.items():
                            courses_num += 1
                            courses_dict[courses_num] = k
                            print(str(courses_num) + '、' + str(k))
                        while True:
                            changed_num = input(
                                '当前学生课程列表为: ' + str(
                                    student_info.courses_list) + ' 请输入您想要添加的课程编号(或输入Q停止添加)：\n>>>').strip()
                            if changed_num.lower() == 'q':
                                break
                            elif int(changed_num):
                                changed_attr.append(courses_dict[int(changed_num)])
                            else:
                                print('对不起，您的输入有误，请重新输入！')
                                continue
                        student_info.courses_list = changed_attr
                    elif modi_attr == '5':
                        while True:
                            learn_record_num = 0
                            print('当前上课记录为: ')
                            for k, v in student_info.learn_record.items():
                                learn_record_num += 1
                                learn_record_dict[learn_record_num] = k
                                print(str(learn_record_num) + '、' + str(k))
                            changed_attr_num = input('请输入您要变更的上课记录-课程名所对应的的编号(或输入Q退出)：\n>>>').strip()
                            if changed_attr_num.lower() == 'q':
                                break
                            elif 0 < int(changed_attr_num) <= learn_record_num:
                                changed_attr_name = learn_record_dict[int(changed_attr_num)].strip()
                                changed_attr_time = input('请输入您要变更的上课记录-上课时间：\n>>>').strip()
                                with open('courses_info.txt', mode='rb') as f:
                                    courses_dict = pickle.load(f)
                                changed_attr_teacher = courses_dict[changed_attr_name][0]
                                student_info.learn_record[changed_attr_name.ljust(10)] = [changed_attr_time,
                                                                                          changed_attr_teacher]
                                is_continue = input('变更成功！是否继续变更上课记录(y/n)?').strip()
                                if is_continue.lower() == 'y':
                                    continue
                                elif is_continue.lower() == 'n':
                                    break
                                else:
                                    print('对不起，你的输入有误，请重新输入！')
                                    continue
                            else:
                                print('对不起，您的输入有误，请重新输入！')
                                continue
                    elif modi_attr.lower() == 'q':
                        break
                    else:
                        print('对不起！您输入的编号有错误，请重新输入！')
                        continue
                    write(student_info.name, 'stuinfo', student_info)
                    print('修改保存成功！当前学生：' + student_info.name + '的信息为：\n性别：' + student_info.sex +
                          '\n年龄：' + student_info.age + '\n密码：' + student_info.password + '\n所选课程：' +
                          str(student_info.courses_list) + '\n学习记录：' + str(student_info.learn_record))

    def show_student(self):
        while True:
            mapping_dict = {}
            print('当前所有学生账号如下：')
            for root, dirs, files in os.walk('./'):
                count = 0
                for i in files:
                    if 'stuinfo.txt' in i:
                        count += 1
                        mapping_dict[count] = i.split('_stuinfo.txt')[0]
                        print(count, i.split('_stuinfo.txt')[0])
            modify_num = input('请输入您要显示学生账号前所对应的编号(或输入Q退出)：\n>>>').strip()
            if modify_num.lower() == 'q':
                break
            else:
                print('您所选择的学生信息如下：')
                file_name = mapping_dict[int(modify_num)] + '_stuinfo.txt'
                with open(file_name, mode='rb') as f_r:
                    student_info = pickle.load(f_r)
                    attr_fields = '''
当前学生%s信息为：
    1、性别 : %s
    2、年龄 : %s
    3、密码 : %s
    4、课程列表 : %s
    5、上课记录 : %s
                    ''' % (student_info.name, student_info.sex, student_info.age, student_info.password,
                           student_info.courses_list, student_info.learn_record)
                    print(attr_fields)

    def add_teacher(self):
        while True:
            teacher_count = 0
            teach_courses = []
            teacher_dict = {}
            try:
                with open('courses_info.txt', mode='rb') as f:
                    courses_dict = pickle.load(f)
            except Exception:
                print('\n对不起，当前还没有教师信息，请添加课程后再使用此功能！谢谢！\n')
                break
            print('欢迎来到完善教师信息功能，根据课程信息，现有教师为：')
            for k, v in courses_dict.items():
                teacher_count += 1
                teacher_dict[teacher_count] = v[0]
                print(str(teacher_count) + '、' + str(v[0]))
            teacher_num = input('请选择要完善信息的教师编号(或输入Q退出)：\n>>>').strip()
            if teacher_num.lower() == 'q':
                break
            elif 0 < int(teacher_num) <= teacher_count:
                name = teacher_dict[int(teacher_num)]
                sex = input('性别：\n>>>').strip()
                age = input('年龄：\n>>>').strip()
                password = input('密码：\n>>>').strip()
                asset = input('资产：\n>>>').strip()
                for k, v in courses_dict.items():
                    if v[0] == name:
                        teach_courses.append(k)
                evaluate_info = {}
                t1 = Teacher(name, sex, age, password, asset, teach_courses, evaluate_info)
                write(name, 'teachinfo', t1)
                is_continue = input('教师' + name + '完善完成！是否继续完善其他教师信息(y/n)?\n>>>').strip()
                if is_continue.lower() == 'y':
                    continue
                elif is_continue.lower() == 'n':
                    break
                else:
                    print('对不起，您的输入有误，请重新输入！')
                    continue
            else:
                print('对不起，您的输入有误，请重新输入！')
                continue

    def delete_teacher(self):
        exit_flag = False
        while not exit_flag:
            print('当前所有教师账号如下：')
            count = 0
            mapping_dict = {}
            for root, dirs, files in os.walk('./'):
                for i in files:
                    if 'teachinfo.txt' in i:
                        count += 1
                        mapping_dict[count] = i.split('_teachinfo.txt')[0]
                        print(count, i.split('_teachinfo.txt')[0])
            delete_num = input('请输入您要\033[1;31m删除\033[0m教师账号前所对应的编号(或输入Q退出)：\n>>>').strip()
            if delete_num.lower() == 'q':
                break
            elif (int(delete_num) > count) or (int(delete_num) < 0):
                print('对不起，您输入的教师编号有误，请重新输入！\n')
                continue
            else:
                file_name = mapping_dict[int(delete_num)] + '_teachinfo.txt'
            print('您所选择的教师信息如下：')
            with open(file_name, mode='rb') as f_r:
                teacher_info = pickle.load(f_r)
                print('\t\t教师姓名：' + str(teacher_info.name) + '\n\t\t性别：' + str(teacher_info.sex) +
                      '\n\t\t年龄：' + str(teacher_info.age) + '\n\t\t资产信息：' + str(teacher_info.asset) +
                      '\n\t\t教授课程：' + str(teacher_info.teach_courses) + '\n\t\t评价信息：' + str(teacher_info.evaluate_info))
            while True:
                is_true = input('\n是否确认要删除该教师账号(y/n)?\n>>>').strip()
                if is_true.lower() == 'y':
                    file_path = './' + file_name
                    os.remove(file_path)
                    print('成功删除教师 ' + mapping_dict[int(delete_num)] + ' 的账号！\n')
                    break
                elif is_true.lower() == 'n':
                    print('欢迎再次使用删除教师账号功能！再见！')
                    exit_flag = True
                    break
                else:
                    print('对不起输入有误！请重新输入！')
                    continue

    def modify_teacher(self):
        while True:
            flag = False
            count1 = 0
            mapping_dict1 = {}
            mapping_dict2 = {}
            print('当前所有教师账号如下：')
            for root, dirs, files in os.walk('./'):

                for i in files:
                    if 'teachinfo.txt' in i:
                        count1 += 1
                        mapping_dict1[count1] = i.split('_teachinfo.txt')[0]
                        print(count1, i.split('_teachinfo.txt')[0])
            modify_num = input('请输入您要修改教师账号前所对应的编号(或输入Q退出)：\n>>>').strip()
            if modify_num.lower() == 'q':
                break
            elif 0 < int(modify_num) <= count1:
                print('您所选择的教师信息如下：')
                file_name = mapping_dict1[int(modify_num)] + '_teachinfo.txt'
                with open(file_name, mode='rb') as f_r:
                    teacher_info = pickle.load(f_r)
                while not flag:
                    attr_fields = '''
当前教师%s信息为：
    1、性别 : %s
    2、年龄 : %s
    3、密码 : %s
    4、资产 : %s
    5、教授课程 : %s
    6、评价信息 : %s
                    ''' % (teacher_info.name, teacher_info.sex, teacher_info.age, teacher_info.password,
                           teacher_info.asset, teacher_info.teach_courses, teacher_info.evaluate_info)
                    print(attr_fields)
                    modi_attr = input('请输入您想要修改的字段的对应编号(或输入Q退出)：\n>>>').strip()
                    if modi_attr == '1':
                        changed_attr = input('当前字段值为: ' + teacher_info.sex + ' 请输入您要变更的字段内容：\n>>>').strip()
                        teacher_info.sex = changed_attr
                    elif modi_attr == '2':
                        changed_attr = input('当前字段值为: ' + teacher_info.age + ' 请输入您要变更的字段内容：\n>>>').strip()
                        teacher_info.age = changed_attr
                    elif modi_attr == '3':
                        changed_attr = input('当前字段值为: ' + teacher_info.password + ' 请输入您要变更的字段内容：\n>>>').strip()
                        teacher_info.password = changed_attr
                    elif modi_attr == '4':
                        changed_attr = input('当前字段值为: ' + teacher_info.password + ' 请输入您要变更的字段内容：\n>>>').strip()
                        teacher_info.asset = changed_attr
                    elif modi_attr == '5':
                        changed_attr = input('当前课程列表为: ' + str(teacher_info.courses_list) +
                                             ' 请输入您要变更的课程列表(用顿号、隔开)：\n>>>').strip().split('、')
                        teacher_info.teach_courses = changed_attr
                    elif modi_attr == '6':
                        while True:
                            count = 0
                            print('当前教师评价信息为: ' + str(teacher_info.evaluate_info))
                            print('当前所有学生账号如下：')
                            for root, dirs, files in os.walk('./'):
                                for i in files:
                                    if 'stuinfo.txt' in i:
                                        count += 1
                                        mapping_dict2[count] = i.split('_stuinfo.txt')[0]
                                        print(count, i.split('_stuinfo.txt')[0])
                            student_num = input('请输入您要变更的评价信息-学生姓名编号(或输入Q退出)：\n>>>').strip()
                            if student_num.lower() == 'q':
                                break
                            elif 0 < int(student_num) <= count:
                                try:
                                    mapping_dict1[int(student_num)]
                                except Exception:
                                    print('对不起，您输入的学生姓名编号有误，请重新输入！')
                                    continue
                            else:
                                print('对不起，您输入的学生编号有误，请重新输入！')
                                continue
                            changed_attr_content = input('请输入您要变更的评价信息-评价内容：\n>>>').strip()
                            changed_attr_name = mapping_dict1[int(student_num)]
                            teacher_info.evaluate_info[changed_attr_name] = \
                                [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), changed_attr_content]
                    elif modi_attr.lower() == 'q':
                        break
                    else:
                        print('对不起！您输入的编号有错误，请重新输入！')
                        continue
                    write(teacher_info.name, 'teachinfo', teacher_info)
                    print('修改保存成功！当前教师：' + teacher_info.name + '的信息为：\n性别：' + teacher_info.sex +
                          '\n年龄：' + teacher_info.age + '\n密码：' + teacher_info.password + '\n所选课程：' +
                          str(teacher_info.teach_courses) + '\n学习记录：' + str(teacher_info.evaluate_info))

    def show_teacher(self):
        while True:
            mapping_dict = {}
            count = 0
            print('当前所有教师账号如下：')
            for root, dirs, files in os.walk('./'):
                for i in files:
                    if 'teachinfo.txt' in i:
                        count += 1
                        mapping_dict[count] = i.split('_teachinfo.txt')[0]
                        print(count, i.split('_teachinfo.txt')[0])
            modify_num = input('请输入您要修改教师账号前所对应的编号(或输入Q退出)：\n>>>').strip()
            if modify_num.lower() == 'q':
                break
            elif 0 < int(modify_num) <= count:
                print('您所选择的教师信息如下：')
                file_name = mapping_dict[int(modify_num)] + '_teachinfo.txt'
                try:
                    with open(file_name, mode='rb') as f_r:
                        teacher_info = pickle.load(f_r)
                        attr_fields = '''
当前教师%s信息为：
    1、性别 : %s
    2、年龄 : %s
    3、密码 : %s
    4、资产 : %s
    5、教授课程 : %s
    6、评价信息 : %s
                        ''' % (teacher_info.name, teacher_info.sex, teacher_info.age, teacher_info.password,
                               teacher_info.asset, teacher_info.teach_courses, teacher_info.evaluate_info)
                        print(attr_fields)
                except Exception:
                    print('对不起，您的输入有误，请重新输入！')
                    continue
            else:
                print('对不起，您的输入有误！')
                continue

    def show_course(self):
        print('当前课程信息为：')
        with open('courses_info.txt', mode='rb') as f_r:
            try:
                courses_dict = pickle.load(f_r)
            except Exception:
                courses_dict = {}
        for k, v in courses_dict.items():
            print(str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) + '\n\t\t课程费用：'
                  + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))

    def add_course(self):
        while True:
            print('当前课程信息为：')
            with open('courses_info.txt', mode='rb') as f_r:
                try:
                    courses_dict = pickle.load(f_r)
                except Exception:
                    courses_dict = {}
            if courses_dict:
                for k, v in courses_dict.items():
                    print(str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) + '\n\t\t课程费用：'
                          + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
            else:
                pass
            new_course = input('请输入要添加的课程名称(或输入Q退出)：\n>>>').strip()
            if new_course.lower() == 'q':
                break
            new_teach = input('请输入该课程的授课教师(或输入Q退出)：\n>>>').strip()
            if new_teach.lower() == 'q':
                break
            new_date = input('请输入该课程的上课时间(或输入Q退出)：\n>>>').strip()
            if new_date.lower() == 'q':
                break
            new_cost = input('请输入该课程的费用(或输入Q退出)：\n>>>').strip()
            if new_cost.lower() == 'q':
                break
            new_content = input('请输入该课程的课程内容(或输入Q退出)：\n>>>').strip()
            if new_content.lower() == 'q':
                break
            courses_dict[new_course] = [new_teach, new_date, new_cost, new_content]
            with open('courses_info.txt', mode='wb') as f_w:
                pickle.dump(courses_dict, f_w)
            print('课程添加完成')

    def delete_course(self):
        while True:
            count = 0
            mapping_course = {}
            print('当前课程信息为：')
            with open('courses_info.txt', mode='rb') as f_r:
                try:
                    courses_dict = pickle.load(f_r)
                except Exception:
                    courses_dict = {}
            for k, v in courses_dict.items():
                count += 1
                mapping_course[count] = k
                print(str(count) + '、' + str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) +
                      '\n\t\t课程费用：' + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
            delete_num = input('请输入要\033[1;31m删除\033[0m的课程名称对应的编号(或输入Q退出)：\n>>>').strip()
            if delete_num.lower() == 'q':
                break
            elif int(delete_num):
                del courses_dict[mapping_course[int(delete_num)]]
                with open('courses_info.txt', mode='wb') as f_w:
                    pickle.dump(courses_dict, f_w)
                print('课程删除完成，当前课程信息为：')
                with open('courses_info.txt', mode='rb') as f_r:
                    courses_dict = pickle.load(f_r)
                    for k, v in courses_dict.items():
                        print(str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) + '\n\t\t课程费用：'
                              + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
                is_continue = input('是否继续删除课程(y/n)？').strip()
                if is_continue.lower() == 'y':
                    continue
                elif is_continue.lower() == 'n':
                    break
                else:
                    print('对不起，您的输入有误，请重新输入！')
                    continue
            else:
                print('对不起，您的输入有误，请重新输入！')
                continue

    def modify_course(self):
        while True:
            count = 0
            mapping_course = {}
            print('当前课程信息为：')
            with open('courses_info.txt', mode='rb') as f_r:
                try:
                    courses_dict = pickle.load(f_r)
                except Exception:
                    courses_dict = {}
            for k, v in courses_dict.items():
                count += 1
                mapping_course[count] = k
                print(
                    str(count) + '、' + str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(
                        v[1]) + '\n\t\t课程费用：'
                    + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
            modify_num = input('请输入要修改的课程名称对应的编号(或输入Q退出)：\n>>>').strip()
            if modify_num.lower() == 'q':
                break
            elif int(modify_num):
                modify_teach = input('请输入该课程的授课教师(或输入Q退出)：\n>>>').strip()
                if modify_teach.lower() == 'q':
                    break
                modify_date = input('请输入该课程的上课时间(或输入Q退出)：\n>>>').strip()
                if modify_date.lower() == 'q':
                    break
                modify_cost = input('请输入该课程的费用(或输入Q退出)：\n>>>').strip()
                if modify_cost.lower() == 'q':
                    break
                modify_content = input('请输入该课程的课程内容(或输入Q退出)：\n>>>').strip()
                if modify_content.lower() == 'q':
                    break
                courses_dict[mapping_course[int(modify_num)]] = [modify_teach, modify_date, modify_cost, modify_content]
                with open('courses_info.txt', mode='wb') as f_w:
                    pickle.dump(courses_dict, f_w)
                print('课程修改完成，当前课程信息为：')
                with open('courses_info.txt', mode='rb') as f_r:
                    courses_dict = pickle.load(f_r)
                    for k, v in courses_dict.items():
                        print(str(k) + ': ' + '\n\t\t课程教师：' + str(v[0]) + '\n\t\t上课时间：' + str(v[1]) + '\n\t\t课程费用：'
                              + str(v[2]) + '\n\t\t课程内容：' + str(v[3]))
                is_continue = input('是否继续修改课程(y/n)？').strip()
                if is_continue.lower() == 'y':
                    continue
                elif is_continue.lower() == 'n':
                    break
                else:
                    print('对不起，您的输入有误，请重新输入！')
                    continue
            else:
                print('对不起，您的输入有误，请重新输入！')
                continue


def main():
    try:
        with open('courses_info.txt', mode='rb') as f_r:
            f_r.read()
    except Exception:
        with open('courses_info.txt', mode='w') as f_w:
            f_w.write(' ')
    while True:
        role = input('欢迎登陆选课系统！\n请选择想要登陆角色所对应的编号:\n1、管理员\n2、学生\n3、教师\n4、\033[1;31m退出\033[0m选课系统\n>>>').strip()
        if role == '1':
            flag = False
            is_exist = input('是否已经拥有管理员账号(y/n)?\n>>>').strip()
            if is_exist.lower() == 'n':
                name = input('新建管理员账号：请输入管理员的姓名：\n').strip()
                password = input('请输入管理员的密码：\n').strip()
                a1 = Admin(name, password)
                write(name, 'admininfo', a1)
                print('管理员' + name + '创建成功！')
            elif is_exist.lower() == 'y':
                name = input('请输入管理员的姓名：\n').strip()
                for root, dirs, files in os.walk('./'):
                    if not flag:
                        for i in files:
                            if (name + '_admininfo.txt') in i:
                                obj_admin = read(name, 'admininfo')
                                userinput_psw = input('请输入管理员 ' + obj_admin.name + ' 的密码\n>>>').strip()
                                if userinput_psw == obj_admin.password:
                                    while True:
                                        print('当前管理员的姓名为：' + obj_admin.name + '\n请选择管理员功能操作：')
                                        print('1、添加课程\n2、删除课程\n3、修改课程\n4、显示课程\n5、添加学生信息\n6、删除学生信息\n'
                                              '7、修改学生信息\n8、显示学生信息\n9、完善教师信息\n10、删除教师信息\n11、修改教师信息\n'
                                              '12、显示教师信息\n13、\033[1;31m退出\033[0m管理员角色')
                                        admin_choice = input('>>>').strip()
                                        if admin_choice == '1':
                                            obj_admin.add_course()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '2':
                                            obj_admin.delete_course()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '3':
                                            obj_admin.modify_course()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '4':
                                            obj_admin.show_course()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '5':
                                            obj_admin.add_student()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '6':
                                            obj_admin.delete_student()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '7':
                                            obj_admin.modify_student()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '8':
                                            obj_admin.show_student()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '9':
                                            obj_admin.add_teacher()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '10':
                                            obj_admin.delete_teacher()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '11':
                                            obj_admin.modify_teacher()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '12':
                                            obj_admin.show_teacher()
                                            write(name, 'admininfo', obj_admin)
                                        elif admin_choice == '13':
                                            break
                                        else:
                                            print('对不起，您的输入有误！')
                                            continue
                                else:
                                    print('对不起，您输入的管理员 ' + obj_admin.name + ' 密码不正确！\n')
                                    flag = True
                                    break
                    elif flag:
                        break
        elif role == '2':
            flag = False
            is_exist = input('是否已经存在学生账号(y/n)?\n>>>').strip()
            if is_exist.lower() == 'n':
                name = input('新建学生账号：请输入学生的姓名：\n').strip()
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
                print('学生' + name + '创建成功！')
            elif is_exist.lower() == 'y':
                name = input('请输入学生的姓名：\n').strip()
                for root, dirs, files in os.walk('./'):
                    if not flag:
                        for i in files:
                            if (name + '_stuinfo.txt') in i:
                                obj_stu = read(name, 'stuinfo')
                                userinput_psw = input('请输入学生 ' + obj_stu.name + ' 的密码\n>>>').strip()
                                if userinput_psw == obj_stu.password:
                                    while True:
                                        print('当前学生的姓名为：' + obj_stu.name + '\n请选择学生功能操作：')
                                        print('1、修改学生信息\n2、上课学习\n3、查询已选课程\n4、查询上课记录\n'
                                              '5、自主选课\n6、\033[1;31m退出\033[0m学生角色')
                                        student_choice = input('>>>').strip()
                                        if student_choice == '1':
                                            obj_stu.modify_stuinfo()
                                            write(name, 'stuinfo', obj_stu)
                                        elif student_choice == '2':
                                            obj_stu.learn_courses()
                                            write(name, 'stuinfo', obj_stu)
                                        elif student_choice == '3':
                                            obj_stu.search_courses()
                                            write(name, 'stuinfo', obj_stu)
                                        elif student_choice == '4':
                                            obj_stu.search_learnrecord()
                                            write(name, 'stuinfo', obj_stu)
                                        elif student_choice == '5':
                                            obj_stu.select_course()
                                            write(name, 'stuinfo', obj_stu)
                                        elif student_choice == '6':
                                            break
                                        else:
                                            print('对不起，您的输入有误！')
                                            continue
                                else:
                                    print('对不起，您输入的学生 ' + obj_stu.name + ' 密码不正确！\n')
                                    flag = True
                                    break
                    elif flag:
                        break
        elif role == '3':
            flag = False
            mapping_dict = {}
            is_exist = input('是否已经存在教师账号(y/n)?\n>>>').strip()
            if is_exist.lower() == 'n':
                name = input('新建教师账号：请输入教师的姓名：\n').strip()
                sex = input('请输入教师的性别：\n').strip()
                age = input('请输入教师的年龄：\n').strip()
                password = input('请输入教师的密码：\n').strip()
                asset = input('请输入教师的密码：\n').strip()
                teach_courses = input('请输入教师的教授课程(用顿号、隔开)：\n>>>').strip().split('、')
                evaluate_info = {}
                while True:
                    print('当前所有学生账号如下：')
                    for root, dirs, files in os.walk('./'):
                        count = 0
                        for i in files:
                            if 'stuinfo.txt' in i:
                                count += 1
                                mapping_dict[count] = i.split('_stuinfo.txt')[0]
                                print(count, i.split('_stuinfo.txt')[0])
                    student_num = input('添加评价信息：\n请输入评价该教师的学生姓名对应的编号：\n>>>').strip()
                    evaluate_info_name = mapping_dict[int(student_num)]
                    evaluate_info_content = input('请输入该学生对此教师的评价：\n>>>').strip()
                    is_continue = input('是否继续添加评价信息(y/n)？\n>>>').strip()
                    if is_continue.lower() == 'y':
                        evaluate_info[evaluate_info_name] = \
                            [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), evaluate_info_content]
                        continue
                    elif is_continue.lower() == 'n':
                        evaluate_info[evaluate_info_name] = \
                            [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), evaluate_info_content]
                        break
                    else:
                        print('对不起！输入有误，请重新输入！')
                t1 = Teacher(name, sex, age, password, asset, teach_courses, evaluate_info)
                write(name, 'teachinfo', t1)
                print('教师' + name + '创建成功！')
            elif is_exist.lower() == 'y':
                name = input('请输入教师的姓名：\n').strip()
                for root, dirs, files in os.walk('./'):
                    if not flag:
                        for i in files:
                            if (name + '_teachinfo.txt') in i:
                                obj_teacher = read(name, 'teachinfo')
                                userinput_psw = input('请输入教师 ' + obj_teacher.name + ' 的密码\n>>>').strip()
                                if userinput_psw == obj_teacher.password:
                                    while True:
                                        print('当前教师的姓名为：' + obj_teacher.name + '\n请选择教师功能操作：')
                                        print('1、修改教师信息\n2、查询教授课程\n3、查询评价记录\n4、\033[1;31m退出\033[0m教师角色')
                                        teacher_choice = input('>>>').strip()
                                        if teacher_choice == '1':
                                            obj_teacher.modify_teachinfo()
                                            write(name, 'teachinfo', obj_teacher)
                                        elif teacher_choice == '2':
                                            obj_teacher.search_teach()
                                            write(name, 'teachinfo', obj_teacher)
                                        elif teacher_choice == '3':
                                            obj_teacher.search_evaluate()
                                            write(name, 'teachinfo', obj_teacher)
                                        elif teacher_choice == '4':
                                            break
                                        else:
                                            print('对不起，您的输入有误！')
                                            continue
                                else:
                                    print('对不起，您输入的教师 ' + obj_teacher.name + ' 密码不正确！\n')
                                    flag = True
                                    break
                    elif flag:
                        break
        elif role == '4':
            print('感谢使用选课系统，欢迎下次光临！再见！')
            exit()
        else:
            print('选择角色有错误！请重新选择！\n')
            continue

if __name__ == '__main__':
    main()
