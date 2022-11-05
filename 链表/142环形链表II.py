# !/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Optional

# @Author: 花菜
# @File: 142环形链表II.py
# @Time : 2022/11/5 17:45
# @Email: lihuacai168@gmail.com

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        # 当快指针为空时，证明已经到了尽头或者为空，不存在环
        while fast and fast.next:
            # 快指针走两步，慢指针走一步
            fast = fast.next.next
            slow = slow.next

            # 快慢指针相遇时，证明存在环
            if fast == slow:
                # 相遇点走到入口的等于从开头走到入口的距离，需要数学证明
                # 在相遇点定义两个新的起点，每次走一步
                # 当他们相等时，证明去到了环的入口
                idx = fast
                idx1 = head

                while idx != idx1:
                    idx = idx.next
                    idx1 = idx1.next

                return idx
        return None
