#!/usr/bin/env python3.6
# coding=utf-8

"""
功能说明：编写登录接口
1、输入用户名密码
2、认证成功后显示欢迎信息
3、输错3次后锁定
"""

def login():
    """
    实现说明：
    1、当前功能仅针对用户信息文件中指定用户进行验证，如果输入不同的用户名仍按指定账号进行验证核实
    2、后续需要改进对已经存在的多个账号信息进行核实：输入的账号是否属于合法用户，属于进行下一步验证，不属于则拒绝登录
    3、通过return实现多重循环的跳出，但未使用while-else结果或for-else结构，因为代码中多次使用break，不利于该结构稳定 
    """
    while True:
        # 该标志位用于标记是否登录成功，0为失败，1为成功
        login_flag = 0
        account_lock_flag = 0

        for i in range(3):
            # 用户输入用户名和密码
            user_name = input("Pls input user name: ")
            password = input("Pls input the password")
            # 存储的用户信息中有一个字段是用户账号的状态，1为正常，0位锁定
            user_status = 1
            # 类型为list，用于读取userinfo文件中持久化的用户信息，如用户名、密码、账号状态等信息
            user_info_stored = None
            account_lock_flag += 1

            # 考虑使用with进行重构操作文件部分的功能
            f4read = open("config/userinfo", "r")
            user_info_stored = f4read.readlines()[0].split(" ")
            f4read.close()
            print("user info stored: %s " % user_info_stored)

            # 登录功能，必须用户名+密码均正确，且用户账号状态为非锁定状态才可以正常登录
            if user_status != int(user_info_stored[3]):
                print("Your account has been locked, pls contact the administrator...")
                break
            elif user_name == user_info_stored[1] and password == user_info_stored[2]:
                login_flag = 1
                print("Login successfully...")
                break
            else:
                print("Username or password is not correct, pls retry...")

            print("account lock flag: %d" % account_lock_flag)

        # 登录重试次数达到3次则重置当前用户的账号状态为锁定状态
        if login_flag == 0 and account_lock_flag == 3:
            # 考虑使用with重构操作文件部分的功能
            f2read4resetStatus = open("config/userinfo", "r")
            user_info4write = f2read4resetStatus.readlines()
            f2read4resetStatus.close()
            # 改写用户信息第四位从1置为0
            user_info4write[0] = user_info4write[0].replace(user_info4write[0][-2:],"0\n")
            print(user_info4write)
            # 将改写的信息重新写入userinfo文件
            f4writeNewStatus = open("config/userinfo", "w")
            f4writeNewStatus.writelines(user_info4write)
            f4writeNewStatus.close()
            # 重试登录三次仍然失败，重置账号状态以后提醒用户：账号已经被锁定
            print("You have tried 3 times to login, and your account has been locked...")
            return 0
        else:
            print("Welcome, %s !" % user_name)
            # 使用return跳出外层循环（推荐），或使用break结束外层循环均可
            return 1

login()

# user_name = input("Pls input user name: ")
# password = input("Pls input the password")
# # 存储的用户信息中有一个字段是用户账号的状态，1为正常，0位锁定
# user_status = 1
# user_info_stored = None
#
#
# # 考虑使用with进行重构读取文件部分
# f = open("config/userinfo", "r")
# user_info_stored = f.readlines()[0].split(" ")
# f.close()
# print(user_info_stored)
#
# # 登录功能，必须用户名+密码均正确，且用户账号状态为非锁定状态才可以正常登录
# if user_name == user_info_stored[1] and password == user_info_stored[2] and user_status == int(user_info_stored[3]):
#     print("Welcome, %s" % user_name)
