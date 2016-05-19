#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def palindrome(st):
    if st == st[::-1]:
        return "String: <" + st + "> is palindrome!"
    else:
        return "String: <" + st + "> is NOT palindrome!"


def palindrome_manual(st):
    reverse_st = ''
    st_len = len(st)

    for c in range(1, st_len + 1):
        reverse_st += st[st_len - c]

    if st == reverse_st:
        return "String: <" + st + "> is palindrome!"
    else:
        return "String: <" + st + "> is NOT palindrome!"


def main(st):
    #print palindrome(st)
    print palindrome_manual(st)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='String to be checked if it is palindrome.')
    parser.add_argument('string', nargs='?')
    arg = parser.parse_args()
    if arg.string:
        main(arg.string)
    else:
        st = raw_input("Type any string: ")
        #print palindrome(st)
        print palindrome_manual(st)
