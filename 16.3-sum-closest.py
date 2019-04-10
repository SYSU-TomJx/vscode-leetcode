#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (38.77%)
# Total Accepted:    286K
# Total Submissions: 704.1K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len < 3:
            return []
        nums.sort()
        visible_ids = []
        closest = target
        margin = 9999
        sum_res = 0
        for i in range(nums_len-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            head, tail = i+1, nums_len-1

            while head < tail:
                sum_res = nums[head] + nums[tail] + nums[i]
                tmp_margin = max(sum_res, target) - min(sum_res, target)
                if tmp_margin < margin:
                    margin = tmp_margin
                    closest = sum_res
                if sum_res < target:
                    head += 1
                elif sum_res > target:
                    tail -= 1
                else:
                    return sum_res
        return closest

