#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # length = len(nums)
        # if length <=1:
        #     return False
        # for i in range(length):
        #     for j in range(i+1, length):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        if len(nums) <=1:
            return False
        buffer={}
        for index,item in enumerate(nums):
            if item in buffer:
                return [buffer[item],index]
            else:
                buffer[target - item]=index
