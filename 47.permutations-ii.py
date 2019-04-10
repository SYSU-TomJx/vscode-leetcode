#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (39.22%)
# Total Accepted:    223.1K
# Total Submissions: 568.6K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#
#
class Solution(object):
    def solver(self, nums, result, tmp_res):
        if len(nums) == 0:
            if tmp_res not in result:
                result.append(tmp_res)
                return
        pre = -9999
        for i in range(len(nums)):
            if pre == nums[i]:
                continue
            self.solver(nums[:i]+nums[i+1:], result, tmp_res+[nums[i]])
            pre = nums[i]

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.solver(nums, res, [])
        return res

