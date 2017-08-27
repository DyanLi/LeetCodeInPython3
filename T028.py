#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for hay_index in range(len(haystack)):
            not_found = 0
            if len(haystack)-hay_index < len(needle):
                break
            for nd_index in range(len(needle)):
                if needle[nd_index] != haystack[hay_index+nd_index]:
                    not_found = 1
                    break
            if not not_found:
                return hay_index
        return -1


class Solution1:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for hay_index in range(len(haystack)-len(needle)+1):
            if haystack[hay_index:hay_index+len(needle)] == needle:
                return hay_index
        return -1
