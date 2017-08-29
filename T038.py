#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        cnt, char, tmp = 0, s[0], ''
        for i in range(len(s)):
            if s[i] != char:
                tmp += str(cnt) + s[i-1]
                char, cnt = s[i], 1
            else:
                cnt += 1
        tmp += str(cnt) + char
        return tmp


if __name__ == '__main__':
    solution = Solution()
    result = solution.countAndSay(10)
    print(result)





