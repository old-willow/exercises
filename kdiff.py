#!/usr/bin/env python
# -*- coding: utf-8 -*-


def kdiff(a, k):
    counts = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if abs(a[i] - a[j]) == k:
                counts += 1

    print('Number of k values appearance: ' + str(counts))
    return counts


if __name__ == '__main__':
    _lengths_cnt = int(raw_input('Enter number of list items: '))
    _lengths_i = 0
    _lengths = []
    _k = int(raw_input('Enter k value: '))

    while _lengths_i < _lengths_cnt:
        _lengths_item = int(raw_input('List item value: '))
        _lengths.append(_lengths_item)
        _lengths_i += 1

    kdiff(_lengths, _k)
