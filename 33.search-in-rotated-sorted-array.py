#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.62%)
# Total Accepted:    373.5K
# Total Submissions: 1.1M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_len = len(nums)
        ids_arr = []
        if num_len == 0:
            return -1
        if num_len == 1:
            if target == nums[0]:
                return 0
            return -1
        front = 0
        rear = 1

        while rear < num_len and nums[rear] >= nums[front]:
            rear += 1
            front += 1

        if rear < num_len:
            part_1 = nums[0:rear]
            part_2 = nums[rear:num_len]
            nums = part_2 + part_1
            ids_1 = []
            ids_2 = []
            for i in range(rear):
                ids_1.append(i)
            while rear < num_len:
                ids_2.append(rear)
                rear += 1
            ids_arr = ids_2 + ids_1
        else:
            for i in range(num_len):
                ids_arr.append(i)
        front = 0
        rear = num_len - 1
        mid = (front+rear)/2
        #search_lst = []
        while front <= rear:
            #search_lst.append(mid)
            if nums[mid] == target:
                return ids_arr[mid]
            elif nums[mid] > target:
                rear = mid - 1
            else:
                front = mid + 1
            mid = (front+rear)/2
        return -1

