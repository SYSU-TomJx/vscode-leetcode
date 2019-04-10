#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.34%)
# Total Accepted:    485.6K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        visible_ids = []
        for i in range(nums_len):

            j = i + 1
            while j < nums_len:
                arr_col = nums[i] + nums[j]
                if -arr_col in nums[j+1:]:
                    ids_set = [nums[i], nums[j], -arr_col]
                    ids_set.sort()
                    if ids_set not in visible_ids:
                        visible_ids.append(ids_set)
                j = j + 1
        return visible_ids
'''
class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        if nums_len < 3:
            return []
        nums.sort()
        visible_ids = []
        for i in range(nums_len-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            head, tail = i+1, nums_len-1

            while head < tail:
                sum_res = nums[head] + nums[tail] + nums[i]
                if sum_res < 0:
                    head += 1
                elif sum_res > 0:
                    tail -= 1
                else:
                    visible_ids.append((nums[head], nums[tail], nums[i]))
                    while head<tail and nums[head] == nums[head+1]:
                        head += 1
                    while tail>head and nums[tail] == nums[tail-1]:
                        tail -= 1
                    head += 1
                    tail -= 1
        return visible_ids


