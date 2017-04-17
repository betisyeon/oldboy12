#!/usr/bin/env python3.6
# coding=utf-8

lucky_num = 13
"""
while True:

    input_num = input("Pls input the num you guess between 0 and 100:")

    guess_num = int(input_num)

    if guess_num > 100 or guess_num < 0:
        print("The num you guessed is not valid...")
    elif guess_num > lucky_num:
        print("The num you guessed is greater than the lucky num...")
    elif guess_num < lucky_num:
        print("The num you guessed is less than the luck num...")
    else:
        print("Bingo...")
        break
"""
input_num = -1
guess_count = 0

#while guess_count<3 and lucky_num!=input_num:
while guess_count<3:

    input_num = int(input("Pls input a integer num which between 0 and 100: "))
    if lucky_num > input_num:
        print("The input_num is less than the lucky num...")
    elif lucky_num < input_num:
        print("The input_num is greater than the lucky num...")
    else:
        print("Bingo!!!")
        break

    guess_count += 1

else: # 如果while循环正常结束会走else，如果非正常结束（如用break）则直接结束不走else
    print("Too many retries!!!")

# if input_num == lucky_num:
#     print("Bingo...")
# else:
#     print("Too many retries!!!")