# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional

# @Author: 花菜
# @File: 24两两交换链表中的节点.py
# @Time : 2022/11/5 17:15
# @Email: lihuacai168@gmail.com

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        # 循环终止条件
        # 当节点数偶数时，cur.next不能为空
        # 当节点数是偶数时，cur.next.next不能为空
        while cur.next is not None and cur.next.next is not None:
            # 交换之前需要把第一个节点和第三个节点保存起来
            temp = cur.next
            temp1 = cur.next.next.next

            # 头结点先指向第二个节点
            cur.next = cur.next.next
            # 头结点的下一个节点指向原来的第一个节点
            cur.next.next = temp
            # 原来第一个节点指向第三个节点
            temp.next = temp1

            # 交换完一次，移动指针到第二个节点
            cur = cur.next.next
        return dummy.next
