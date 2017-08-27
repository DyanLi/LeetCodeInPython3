#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C':100, 'D': 500, 'M':1000 }
        result = 0
        for item in s[::-1]:
            if (item in ['I', 'X', 'C']) and result >= 5 * dict[item]:
                result -= dict[item]
            else:
                result += dict[item]
        return result