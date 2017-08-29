#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0
        if nums[len(nums) - 1] < target:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] >= target:
                return i


if __name__ == '__main__':
    solution = Solution()
    result = solution.searchInsert([1,3,5,6],3)
    print(result)
