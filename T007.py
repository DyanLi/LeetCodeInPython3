#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = list(str(x))
        for i in range(len(l)//2 + 1):
            if l[i] != l[len(l) - i]:
                return False
        return True
