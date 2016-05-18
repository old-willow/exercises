#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print 'FizzBuzz'
        elif i % 3 == 0:
            print 'Fizz'
        elif i % 5 == 0:
            print 'Buzz'
        else:
            print i


if __name__ == '__main__':
    n = int(raw_input("Enter a number: "))
    fizzbuzz(n)
