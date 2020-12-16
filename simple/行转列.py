# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 行转列.py
# @Time : 2020/12/16 10:56
# @Email: lihuacai168@gmail.com

def row2col(rows):
    """
    行转列
    >>> a0 = "861193040851470|1607652227|3303944933|2|1607651868|360|1607651868".split("|")
    >>> a1 = "861193040851470|1607652228|3303944933|2|1607651868|360|1607651868".split("|")
    >>> a2 = "861193040851470|1607652229|3303944933|2|1607651868|360|1607651868".split("|")
    >>> row2col([a0, a1 , a2])
    [['861193040851470', '861193040851470', '861193040851470'], ['1607652227     ', '1607652228     ', '1607652229     '], ['3303944933     ', '3303944933     ', '3303944933     '], ['2              ', '2              ', '2              '], ['1607651868     ', '1607651868     ', '1607651868     '], ['360            ', '360            ', '360            '], ['1607651868     ', '1607651868     ', '1607651868     ']]
    """

    max_col_len = len(max(rows[0], key=len))
    row_len = len(rows[0])
    col_len = len(rows)
    cols = [[] for _ in range(row_len)]
    for i in range(row_len):
        for j in range(col_len):
            cols[i].append(rows[j][i].ljust(max_col_len, ' '))
    return cols


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
