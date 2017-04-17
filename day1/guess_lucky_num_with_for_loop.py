#!/usr/bin/env python3.6
# coding=utf-8

lucky_num = 13

for i in range(3):

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
else: #for正常结束会走else，如果非正常结束则不会走else
    print("Too many tries!!!")