# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional

# @Author: 花菜
# @File: 19删除链表的倒数第N个结点.py
# @Time : 2022/11/5 17:21
# @Email: lihuacai168@gmail.com

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        # 快慢指针
        # 要删除倒数第n个节点，因此需要找到倒数第n+1个节点
        # 让快指针先走n+1步
        # 快慢指针再同时遍历，快指针始终比慢指针多n+1步
        # 到链表结束，此时慢指针就是倒数第n个节点

        i = 0
        # 快指针移动n+1步
        # 因为要输出删除数n个节点，实际上操作是倒数n+1个节点
        while i <= n:
            i += 1
            fast = fast.next

        # 同时移动快慢指针，指导快指针为空
        while fast:
            fast = fast.next
            slow = slow.next
        # 退出，循环结束时，快指针为空
        # 慢指针在快指针的倒数第三个

        # 删除倒数n个节点
        slow.next = slow.next.next

        return dummy.next


def build_list_node(arr):
    head = ListNode()
    cur = head
    for i in arr:
        cur.next = ListNode(i)
        cur = cur.next
    return head.next


def test_del_nnode():
    arr = [1, 2, 3, 4, 5, 6]
    head = build_list_node(arr)

    s = Solution()
    s.removeNthFromEnd(head, 2)
    print(s)


if __name__ == "__main__":
    test_del_nnode()
