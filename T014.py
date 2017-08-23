#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs_len = list(map(lambda x: len(x), strs))
        min_len = min(strs_len)
        sd_str = strs[strs_len.index(min_len)]
        end = 0
        for i in range(min_len):
            flag_no = 0
            for item in strs:
                if sd_str[i] != item[i]:
                    flag_no = 1
                    break
            if flag_no:
                break
            end +=1

        return sd_str[:end]

