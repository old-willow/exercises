#!/usr/bin/env python
# -*- coding: utf-8 -*-


#import sys


def StairCase(n):
    for i in range(1, n + 1):
        space = n - i
        stair = i
        print ' ' * space + '#' * stair


def sum_int_in_list(n, nums):
    sum_num = sum(nums)
    print sum_num


if __name__ == '__main__':
    num = int(raw_input("Type number of stairs: "))
    StairCase(num)

    n = raw_input("Type number of integer: ")
    n = int(n)
    nums = []
    for i in range(n):
        e = raw_input("Type numbers of integer: ")
        nums.append(int(e))

    sum_int_in_list(n, nums)
