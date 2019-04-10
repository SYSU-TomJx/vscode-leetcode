#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (53.51%)
# Total Accepted:    343K
# Total Submissions: 640.8K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
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
            #if i > 0:
            #    self.solver(nums[:i]+nums[i+1:], result,[nums[i]]+tmp_res, length)


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.solver(nums, res, [])
        return res


