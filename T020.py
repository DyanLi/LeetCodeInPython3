#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 ==1 :
            return False
        dict = {'(':')', '{':'}', '[':']'}
        stack = []

        for item in s:
            if item in dict.keys():
                stack.append(item)
            else:
                try:
                    match = stack.pop()
                    if not dict[match] ==item:
                        return False
                except:
                    return False

        if not stack:
            return True
        else:
            return False

