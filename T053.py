#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -2**31
        for head in range(len(nums)):
            for tail in range(head+1, len(nums)+1):
                print(nums[head:tail])
                now_sum = sum(nums[head: tail])
                if now_sum > max_sum:
                    max_sum = now_sum
        return max_sum

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = cur_sum = nums[0]
        for tail in range(1,len(nums)):
            cur_sum = max(nums[tail], cur_sum+nums[tail])
            max_sum = max(max_sum, cur_sum)

        return max_sum



if __name__ == '__main__':
    solution = Solution()
    result = solution.maxSubArray2([-2,4,-1])
    print(result)
