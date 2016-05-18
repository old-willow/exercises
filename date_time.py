#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
#import datetime as dt
from datetime import datetime, timedelta
import calendar


def current_date_time():
    return datetime.now()


def current_year():
    return datetime.now().year


def current_month():
    return datetime.now().month


def current_week_of_year():
    today = datetime.now()
    return today.isocalendar()[1]


def current_day_of_week():
    today = datetime.now()

    #return today.weekday()  # English
    return today.isoweekday()  # Serbian


def current_day_of_year():
    return time.localtime().tm_yday


def current_day():
    return datetime.now().day


def current_tzinfo():
    info = datetime.tzinfo

    return info


def sleep_func(sec):
    time.sleep(sec)
    print('Hello Wold!')


def calendar_of_year(year):
    print(calendar.calendar(year))


def calendar_of_the_month(year, month):
    print(calendar.month(year, month))


# 'true' if True else 'false'
def is_leap(year):
    l = calendar.isleap(year)
    #if l:
    #    print('Year ' + str(year) + ' is leap.')
    #else:
    #    print('Year ' + str(year) + ' is not leap.')
    print('Year ' + str(year))
    print('Is leap year.' if l else 'Is not leap year.')


def string_to_datetime(date_string):
    d = datetime.strptime(date_string, '%b %d %Y')
    print d
    return d


def this_year_birthday_of_anna(d):
    day_name = d.strftime('%A')
    print day_name
    return day_name


def current_time():
    #d = datetime.now().strftime('%H:%M')
    #print(d)
    d = datetime.now().time()
    print(d)
    return d


def subtract_days_from_current_date(days):
    today = datetime.now()
    old_date = today - timedelta(days=days)
    print old_date
    return old_date


def convert_unix_timestamp_to_human_readable(ts):
    hr = datetime.fromtimestamp(ts).strftime('%d.%m.%Y.  -  %H:%M:%S')
    print(hr)
    return hr


def print_ytt():
    """
    ytt => yesterday, today, tomorrow;
    """
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print("Yesterday was: %s" % (yesterday, ))
    print("Today is: %s" % (today, ))
    print("Tomorrow will be: %s" % (tomorrow, ))

    return (yesterday, today, tomorrow, )


def convert_date_to_datetime(date):
    dt = date.today()
    today_midnight = datetime.combine(dt, datetime.min.time())
    print today_midnight
    return today_midnight


def next_5_days():
    today = datetime.now()

    for i in range(1, 6):
        next = today + timedelta(days=i)

        if i == 1:
            singular = 'day'
        else:
            singular = 'days'

        print("%s %s from today: %s - %s" % (i, singular, next.strftime('%d.%m.%Y.'), next.strftime('%A')))


if __name__ == '__main__':
    print 'Current date and time: ', current_date_time()
    print 'Current year: ', current_year()
    print 'Current month: ', current_month()
    print 'Current day: ', current_day()
    print 'Time zone info: ', current_tzinfo()

    #sleep_func(1)
    #calendar_of_year(1977)
    #calendar_of_the_month(1999, 9)
    #is_leap(1999)

    print 'The week of the year', current_week_of_year()
    print 'The day of the year', current_day_of_year()
    date_string = "Jun 1 2016"
    birth_day = string_to_datetime(date_string)
    print("This year Anna's birthday is on %s" % this_year_birthday_of_anna(birth_day))
    print("Current time is: %s" % current_time())

    days_before = 5
    old_day = subtract_days_from_current_date(days_before)
    print("%s days ago was %s - %s." % (days_before, old_day.date(), old_day.strftime('%A')))

    print('********************************')
    ts = time.time()
    print('Unix time stamp: %s' % ts)
    convert_unix_timestamp_to_human_readable(ts)
    print_ytt()
    print('********************************')
    d = datetime.date(datetime.now())
    convert_date_to_datetime(d)

    next_5_days()
