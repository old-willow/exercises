#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
import unittest


def separate_lengths(*lst):
    a, b = lst
    #print "A: ", a
    #print "B: ", b
    longest = max(lst)
    smallest = min(lst)
    return (longest, smallest, )


def list_common(*lst):
    common_set = []
    longest, smallest = separate_lengths(*lst)

    for i in range(len(longest)):
        for j in range(len(smallest)):
            if longest[i] == smallest[j] and smallest[j] not in common_set:
                common_set.append(longest[i])

    return common_set


def list_difference(*lst):
    diff_set = []
    longest, smallest = separate_lengths(*lst)

    for i in range(len(longest)):
        if longest[i] not in smallest:
            diff_set.append(longest[i])

    for i in range(len(smallest)):
        if smallest[i] not in longest:
            diff_set.append(smallest[i])

    return diff_set


class TestCommon(unittest.TestCase):
    """
    RESULT:
    commont: [1, 2, 3, 5, 8, 13, ]
    """
    def setUp(self):
        self.a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def tearDown(self):
        del self.a
        del self.b

    def test_common(self):
        result = [1, 2, 3, 5, 8, 13, ]
        self.assertEqual(list_common(self.a, self.b), result)


class TestDifference(unittest.TestCase):
    """
    RESULT:
    diff:    [4, 6, 7, 9, 10, 11, 12, 21, 34, 55, 89, ]
    """
    def setUp(self):
        self.a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def tearDown(self):
        del self.a
        del self.b

    def test_common(self):
        result = [4, 6, 7, 9, 10, 11, 12, 21, 34, 55, 89, ]
        self.assertEqual(list_difference(self.a, self.b), result)


def main(argv):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print "List A:", a
    print "List B:", b

    try:
        opts, args = getopt.getopt(argv, 'hcdt', ['help', 'common', 'diff', 'run-test'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-c', '--common'):
            common_set = list_common(a, b)
            print "Common elements in two array are:", common_set
            #print arg
            #return (arg, common_set)
            return True
        elif opt in ('-d', '--diff'):
            diff_set = list_difference(a, b)
            print "Elements that differ in two array are:", diff_set
            #print arg
            #return (arg, diff_set)
            return True
        elif opt in ('-r', '--run-test'):
            #unittest.main()
            return False


def usage():
    print("Type: python list_overlap.py -h or --help\n"
          "for this help to show up.\n"
          "-d or --diff for calculating difference in lists.\n"
          "-c or --common for calculating common elements in lists.\n"
          "-t or --test for run builtin tests.\n")


if __name__ == '__main__':

    if len(sys.argv) > 1:
        # Found answer at:
        # http://stackoverflow.com/questions/1029891/python-unittest-is-there-a-way-to-pass-command-line-options-to-the-app
        # You have to delete arguments if you want to use arguments with script
        # in order to run tests.
        # Otherwise it will not run tests if I add -t flag to command line.
        result = main(sys.argv[1:])
        print result
        if not result:
            del sys.argv[1:]
            unittest.main()
    else:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        print "List A:", a
        print "List B:", b
        common_set = list_common(a, b)
        print "Common elements in two array are:", common_set
        diff_set = list_difference(a, b)
        print "Elements that differ in two array are:", diff_set

        unittest.main()
