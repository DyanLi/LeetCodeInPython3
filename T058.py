#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        return len(s.strip().split(" ")[-1])
