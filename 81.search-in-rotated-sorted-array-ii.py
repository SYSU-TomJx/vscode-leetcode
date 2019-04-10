#
# @lc app=leetcode id=81 lang=python
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.49%)
# Total Accepted:    160.8K
# Total Submissions: 495K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true,
# otherwise return false.
#
# Example 1:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
#
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
#
#
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)/2
            if nums[mid] == target:
                return True
            while left<mid and nums[left]==nums[mid]:
                left = left + 1
            if nums[left]<=nums[mid]:
                if target>=nums[left] and target<nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if target>nums[mid] and target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False



