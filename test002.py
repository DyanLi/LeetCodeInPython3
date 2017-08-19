#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from T002 import ListNode,Solution

def init_list(list):
    if not list:
        return None
    ln = ListNode(list[0])
    list.pop(0)
    ln.next = init_list(list)
    return ln

def get_ele(node):
    while node:
        print(node.val)
        if node.next:
            node = node.next
        else:
            break

l1 = init_list([4,3])
l2 = init_list([5,6,4])
# get_ele(l1)
solution = Solution()
l3 = solution.addTwoNumbers(l1,l2)
get_ele(l3)

