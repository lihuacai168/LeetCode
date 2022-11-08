# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: helper.py
# @Time : 2022/11/8 16:53
# @Email: lihuacai168@gmail.com


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_single_list_node(arr: list):
    head = ListNode()
    cur = head

    for i in arr:
        cur.next = ListNode(i)
        cur = cur.next
    return head
