#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (40.24%)
# Total Accepted:    202.6K
# Total Submissions: 503.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
#
#
#
class Solution(object):
    def solver(self, candidates, target, result, tmp_res, pos):
        if target == 0:
            if tmp_res not in result:
                result.append(tmp_res)
            return
        if target < 0:
            return
        for i in range(pos, len(candidates)):
            if target - candidates[i] < 0:
                return
            self.solver(candidates, target-candidates[i],
                  result,tmp_res+[candidates[i]], i+1)
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        self.solver(candidates, target, results, [], 0)
        return results
