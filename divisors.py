#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt


def divisors(num):
    divs = []

    try:
        num = int(num)
        for n in range(2, num - 1):
            if not num % n:
                divs.append(str(n))
    except ValueError:
        print "You din't entered number.\nPlease enter a number."
    else:
        print "You have entered the number."
    finally:
        print "Anyway good try."

    if len(divs) == 0:
        return None
    else:
        return divs


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hn:', ['help', 'number='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-n', '--number'):
            print arg
            divs = divisors(arg)
            return (arg, divs)


def usage():
    print("Type divisor.py -h or --help"
          " for this help to show up.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        num, divs = main(sys.argv[1:])
        print divs
    else:
        num = raw_input("type a number: ")
        divs = divisors(num)
    if divs:
        st = ','.join(divs)
        print "Divisors of number " + num + " are: " + '[' + st + ']'
