#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (46.10%)
# Total Accepted:    189.1K
# Total Submissions: 408.1K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
# Example:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
#
class Solution(object):
    def solver(self, nums, res, item, k):
        if k == 0:
            res.append(item)
            return
        for i in range(len(nums)):
            if i == 0:
                self.solver(nums[1:], res, item+[nums[i]], k-1) # if len(nums) == 1, then nums[1:] == []
            else:
                self.solver(nums[i+1:], res, item+[nums[i]], k-1)
    def solver_2(self, nums, index, res, item, k):
        if k == 0:
            res.append(item)
        for i in range(index, len(nums)):
            self.solver_2(nums, i+1, res, item+[nums[i]], k-1)
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))
        res = []
        item = []
        #self.solver(nums, res, item, k)
        self.solver_2(nums, 0, res, item, k)
        return res


