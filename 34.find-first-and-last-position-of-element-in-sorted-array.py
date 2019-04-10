#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.01%)
# Total Accepted:    270.3K
# Total Submissions: 818.7K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res_lst = []
        if nums == []:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        front = 0
        num_len = len(nums)
        rear = (num_len - 1)/2
        mid = (rear+front)/2
        while rear >=front:
            if nums[mid] == target:
                res_lst = [mid] +res_lst
                rear = mid - 1
            else:
                front = mid + 1
            mid = (front+rear)/2
        rear = num_len - 1
        front = rear/2
        mid = (front+rear)/2
        while rear >= front:
            if nums[mid] == target:
                res_lst.append(mid)
                front = mid + 1
            else:
                rear = mid - 1
            mid = (front+rear)/2
        if res_lst == []:
            return [-1, -1]
        return res_lst
'''
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]