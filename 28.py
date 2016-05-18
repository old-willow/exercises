#!/usr/bin/env python
# -*- coding: utf-8 -*-


def max_of_3():
    usr_input = raw_input("Type 3 integer numbers [separated by space]: ")
    print usr_input

    biggest = 0

    num_list = [int(i) for i in usr_input.split()]

    if num_list[0] > num_list[1]:
        biggest = num_list[0]
    elif num_list[0] <= num_list[1]:
        biggest = num_list[1]

    if biggest < num_list[-1]:
        biggest = num_list[-1]

    print biggest


def max_of_many():
    usr_input = raw_input("Type any number of integer numbers [separated by space]: ")
    my_list = [int(i) for i in usr_input.split()]

    biggest = 0

    for i in range(len(my_list)):
        if my_list[i] > biggest:
            biggest = my_list[i]

    print biggest
    return biggest

if __name__ == '__main__':
    #max_of_3()
    max_of_many()
