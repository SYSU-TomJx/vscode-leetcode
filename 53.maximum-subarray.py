#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.84%)
# Total Accepted:    471.5K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#
'''
class Solution(object):
    max_sum = 0
    max_lst = []
    sum_lst = []
    visited = []
    def solver(self, nums, head, tail, sum_res):
        if head > tail or head >= len(nums):
            return
        if self.visited[head] != -1 and self.visited[tail] != -1:
            return
        if sum_res >= self.max_sum:
            self.sum_lst.append
            self.max_sum = sum_res
            self.max_lst = nums[head:tail+1]
        self.solver(nums, head+1, tail, sum_res-nums[head])
        self.solver(nums, head, tail-1, sum_res-nums[tail])
        self.visited[head] = 1
        self.visited[tail] = 1

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = len(nums) - 1
        head = 0
        self.max_lst = nums
        self.max_sum = 0
        for n in nums:
            self.max_sum = self.max_sum + n
            self.visited.append(-1)
        self.solver(nums, head, tail, self.max_sum)
        return self.max_sum

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        for n  in nums:
            max_sum = max_sum + n
        rear = len(nums) - 1
        head = 0
        c = [max_sum]
        p = [max_sum]
        while head < rear:
            p_sum = p[-1]
            f_res = p_sum - nums[rear]
            r_res = p_sum - nums[head]
            if f_res > r_res:
                rear -= 1
                p.append(f_res)
                c.append(max(max_sum, f_res))
            else:
                head += 1
                p.append(r_res)
                c.append(max(max_sum, r_res))
        return p
'''

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_res = nums[0]
        for i in range(1, len(nums)):
            cur_res = max(cur_res+nums[i], nums[i])
            max_sum = max(cur_res, max_sum)
        return max_sum
