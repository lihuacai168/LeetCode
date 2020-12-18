# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: 两数相加.py
# @Time : 2020/12/18 23:01
# @Email: lihuacai168@gmail.com


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''
        head = l1

        while head.next:
            num1 += str(head.val)
            head = head.next
        num1 += str(head.val)

        head = l2
        while head.next:
            num2 += str(head.val)
            head = head.next
        num2 += str(head.val)
        ansStr = str(int(num1[::-1]) + int(num2[::-1]))
        ans = ListNode(ansStr[-1])
        head = ans
        i = len(ansStr) - 2
        while i > -1:
            head.next = ListNode(int(ansStr[i]))
            head = head.next
            i -= 1
        return ans


def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: ListNode):
    while l:
        print(l.val)
        l = l.next
    print('')


if __name__ == "__main__":
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)
