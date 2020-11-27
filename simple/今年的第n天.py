# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 今年的第n天.py
# @Time : 2020/11/27 00:50
# @Email: lihuacai168@gmail.com
import datetime


def get_n_day(date_str: str):
    """
    >>> get_n_day('20200101')
    1

    >>> get_n_day('20200102')
    2

    >>> get_n_day('20201231')
    366

    >>> get_n_day('20211127')
    '日期不在今年之内'

    >>> get_n_day('20181127') == '日期不在今年之内'
    True

    >>> err_msg = "输入日期格式错误,正确格式是：20201127"
    >>> get_n_day('2020-11-27') == err_msg
    True

    >>> get_n_day('202011270') == err_msg
    True

    >>> get_n_day(20200101) == err_msg
    True

    >>> get_n_day("") == err_msg
    True

    """
    try:
        end_day = datetime.datetime.strptime(date_str, '%Y%m%d')
    except Exception as e:
        return "输入日期格式错误,正确格式如：20201127"

    begin_day = datetime.datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    n_day = (end_day - begin_day).days + 1

    if n_day < 0 or n_day > 366:
        return "日期不在今年之内"
    return n_day

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
