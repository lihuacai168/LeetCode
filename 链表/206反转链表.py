# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional

# @Author: 花菜
# @File: 206反转链表.py
# @Time : 2022/11/5 14:34
# @Email: lihuacai168@gmail.com


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 双指针法，prev初始化为空
        # 遍历链表
        # 要操作当前节点，需要先保存当前节点的下一个节点
        # 把当前节点指向prev，到这里当个节点翻转已经完成

        # 需要更新循环变量，当前节点，在下一次循环就是prev节点
        # 当前节点的下一个节点，就是下一次循环的当前节点

        # 循环结束时，prev就原始链表的最后节点，
        # 翻转完成后，prev就变成了头结点
        cur = head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _reverseList(prev, cur):
            if cur is None:
                return prev
            tmp = cur.next
            cur.next = prev
            return _reverseList(cur, tmp)

        return _reverseList(None, head)

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return head
    #
    #     prev = self.reverseList(head.next)
    #
    #     head.next.next = head
    #     head.next = None
    #     return prev


if __name__ == "__main__":
    from helper import build_single_list_node

    head = build_single_list_node([1, 2, 3, 4, 5])

    s = Solution()
    reversed_head = s.reverseList(head)
    print(reversed_head)
