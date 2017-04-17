#!/usr/bin/env python3.6
# coding=utf-8

name = input("Name: ").strip()
age = input("Age: ")
job = input("Job: ").strip()

personal_info = '''

Information of Name: %s
    Name: %s
    Age: %s
    Job: %s

''' % (name, name, age, job)

print(personal_info) # 段落样式打印
print("Information of %s\n Name: %s\n Age: %s\n Job: %s\n" % (name, name, age, job))