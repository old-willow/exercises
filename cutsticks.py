#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cutSticks(lengths):
    _lengths = []  # list without zeros.
    __lengths = lengths  # copy of the original list of sticks on which will be operated.

    # collecting non zero list elements to exclude zero's when caching the
    # smallest value in the list
    for x in range(len(lengths)):
        for i in __lengths:
            if i != 0:
                _lengths.append(i)

        # chosing the smallest value from zeroless list
        smallest = min(_lengths)
        new_list = []  # the new list to which will be added the calculated part and the zeros.

        # run again through the copy of the original for calculation.
        for i in __lengths:
            if i == 0:
                new_list.append(0)
            else:
                new_list.append(i - smallest)

        print new_list

        __lengths = new_list


if __name__ == '__main__':

    _lengths_cnt = int(raw_input())
    _lengths_i = 0
    _lengths = []

    while _lengths_i < _lengths_cnt:
        _lengths_item = int(raw_input())
        _lengths.append(_lengths_item)
        _lengths_i += 1

    cutSticks(_lengths)
