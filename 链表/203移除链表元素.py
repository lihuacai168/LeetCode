# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional

# @Author: 花菜
# @File: 203移除链表元素.py
# @Time : 2022/11/5 14:30
# @Email: lihuacai168@gmail.com

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre = ListNode()
        # 定义一个虚拟头结点，指向head
        # 目的是统一删除的操作
        # 不然删除头结点和其他节点的操作是不一样
        pre.next = head
        # 需要新定义一个指针来操作链表
        # 直接用pre删除的话，最后无法返回原来的head
        cur = pre

        while cur.next:
            # 删除单向链表节点时，是需要知道节点的前一个节点
            # 所以需要判断cur.next
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        # 不能返回head，因为val等于head.val时，是需要删除的
        return pre.next
