#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (46.81%)
# Total Accepted:    308.3K
# Total Submissions: 658.6K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
#
class Solution(object):
    def solver(self, candidates, target, results, sub_res, pos):
        if target == 0:
            results.append(sub_res)
            sub_res = []
            return
        if target < 0:
            return
        pre = -99999
        #tmp_res = list(sub_res)
        for i in range(pos, len(candidates)):
            if target-candidates[i] < 0:
                return
            if pre == candidates[i]:
                continue
            #tmp_res.append(candidates[i])
            self.solver(candidates,
                        target-candidates[i],
                        results, sub_res+[candidates[i]], i)
            #tmp_res = tmp_res[0:-1]
            pre = candidates[i]
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.solver(candidates, target, res, [], 0)
        return res
