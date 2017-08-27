#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n_flag = 0 if x >= 0 else 1
        x = abs(x)
        output = int(''.join(reversed(list(str(x)))))
        if (output > 2 ** 31):
            return 0
        if n_flag:
            return 0 - output
        else:
            return output

