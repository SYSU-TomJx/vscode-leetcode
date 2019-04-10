#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (41.88%)
# Total Accepted:    195.2K
# Total Submissions: 466.1K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#
#
class Solution(object):
    '''
    def solver(self, nums, res):
        if nums not in res:
            res.append(nums)
        else:
            return
        if len(nums)<=1:
            return
        for i in range(len(nums)):
            if i == 0:
                tmp_nums = nums[1:]
            else:
                tmp_nums = nums[0:i]+nums[i+1:]
            self.solver(tmp_nums, res)
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.solver(nums, res)
        res.append([])
        return res

    def subsetsWithDup(self, nums):
        result = [[]]
        for num in sorted(nums):
            result += [i+[num] for i in result if i+[num] not in result]
        return result
    '''
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)
