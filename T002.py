#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = node = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            node.next = ListNode(val)
            node = node.next
        return root.next


            #     if l1 and l2:
    #         return self.calc_list(l1,l2,0)
    #
    # def calc_list(self, l1, l2, flag):
    #     s1 = l1.val if l1 else 0
    #     s2 = l2.val if l2 else 0
    #     s = s1 + s2
    #     if s > 9:
    #         l3 = ListNode(s + flag - 10)
    #         flag = 1
    #     else:
    #         l3 = ListNode(s + flag)
    #         flag = 0
    #
    #     if l1.next and l2.next:
    #         l1 = l1.next
    #         l2 = l2.next
    #         l3.next = self.calc_list(l1, l2, flag)
    #     else:
    #         if l1.next:
    #             l4 = l1.next
    #             l4.val += flag
    #             l3.next = l4
    #         elif l2.next:
    #             l4= l2.next
    #             l4.val += flag
    #             l3.next = l4
    #         elif flag:
    #             l3.next = ListNode(1)
    #
    #     return l3





