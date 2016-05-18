#!/usr/bin/env python
# -*- coding: utf-8 -*-


def less_then_5(l):
    new_l = []

    for i in l:
        if i < 5:
            new_l.append(i)

    return new_l


if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    my_list = less_then_5(a)
    print my_list
