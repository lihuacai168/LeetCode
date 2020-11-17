# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author:梨花菜
# @File: LinkList.py
# @Time : 2020/9/3 22:10
# @Email: lihuacai168@gmail.com
# @Software: PyCharm

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList:
    """
    is_empty(self):
    判断链表是否为空

    length(self):
    链表长度

    travel(self):
    遍历整个链表

    add(self, item):
    头部增加元素

    append(self, item):
    尾部插入

    insert(self,pos, item):
    指定位置插入元素

    remove(self, item):
    删除节点


    search(self, item):
    查找元素
    """

    def __init__(self, node=None):
        if node is not None:
            self._head = Node(node)
        else:
            self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        index = self._head
        count = 0
        while index is not None:
            count += 1
            index = index.next
        return count

    def travel(self):
        index = self._head
        while index is not None:
            print(index.elem)
            index = index.next

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node

        else:
            index = self._head
            while index.next is not None:
                index = index.next
            index.next = node

    def insert(self, pos, item):
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            index = self._head
            for i in range(self.length()):
                index = index.next
                if i == pos - 1:
                    node.next = index.next
                    index.next = node
                    break

    def search(self, item):
        if self.is_empty() is True:
            return False
        index = self._head
        for _ in range(self.length()):
            if index.elem == item:
                return True
            else:
                index = index.next
        return False

    def remove(self, item):

        cur = self._head
        pre = None

        while cur is not None:
            if cur.elem == item:
                if pre is None:
                    self._head = cur.next
                    break
                else:
                    pre.next = cur.next
                    break
                # break
            pre = cur
            cur = cur.next

        # if self.search(item) is False:
        #     raise Exception("item is not exist")
        # index = self._head
        # if index.elem == item:
        #     self._head = index.next
        #     return
        #
        # for _ in range(self.length() - 1):
        #     if index.next.elem == item:
        #         if index.next is not None:
        #             index.next = index.next.next
        #         else:
        #             index.next = None
        #         break
        #     else:
        #         index = index.next


def test_is_empty():
    sll = SingleLinkList()
    assert sll.is_empty() is True


def test_is_not_empty():
    node = Node(22)
    sll_not_empty = SingleLinkList(node=node)
    assert sll_not_empty.is_empty() is False


def test_length():
    node = Node(22)
    sll_1 = SingleLinkList(node=node)
    sll_0 = SingleLinkList()
    assert sll_1.length() == 1
    assert sll_0.length() == 0


def test_append_empty():
    sll_0 = SingleLinkList()
    sll_0.append(233)
    assert sll_0.length() == 1
    sll_0.append(2344)
    assert sll_0.length() == 2


if __name__ == '__main__':
    sll_0 = SingleLinkList()
    assert sll_0.search(1) is False
    sll_0.append(0)
    sll_0.append(1)
    sll_0.append(2)
    sll_0.append(3)
    sll_0.append(3)
    # sll_0.add(123)
    # sll_0.add(1)
    # sll_0.insert(1, 900)
    # sll_0.insert(4, 400)
    sll_0.insert(0, 400)
    sll_0.insert(-1, -100)
    sll_0.insert(10, 10)
    assert sll_0.search(400) is True
    assert sll_0.search(401) is False
    sll_0.remove(3)
    sll_0.remove(10)
    sll_0.remove(-100)
    sll_1 = SingleLinkList('a')
    sll_1.remove('a')
    sll_0.travel()
    sll_1.travel()
