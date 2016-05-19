#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(ls):
    """
    Return even numbers from the list
    """
    new_ls = []
    [new_ls.append(l) for l in ls if l % 2 == 0]

    return new_ls


if __name__ == '__main__':
    ls = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
    new_ls = main(ls)

    print new_ls


