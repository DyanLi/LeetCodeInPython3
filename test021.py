#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from T021 import ListNode, Solution

def init_list(list):
    if not list:
        return None
    ln = ListNode(list[0])
    list.pop(0)
    ln.next = init_list(list)
    return ln

def print_list(node):
    while node:
        print(node.val)
        if node.next:
            node = node.next
        else:
            break


solution = Solution()
l1 = init_list([1,5,8,10])
l2 = init_list([2,6,8,12,16])
l3 = solution.mergeTwoLists(l1,l2)
print_list(l3)
