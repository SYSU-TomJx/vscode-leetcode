#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (53.04%)
# Total Accepted:    304K
# Total Submissions: 570.9K
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
class Solution(object):
    def solver(self, result, cur_str, left, right):
        if left==0 and right==0:
            result.append(cur_str)
            return
        if left > 0:
            self.solver(result, cur_str+'(', left-1, right)
        if right > 0 and right > left:
            self.solver(result, cur_str+')', left, right-1)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n <= 0:
            return result
        self.solver(result, '', n, n)
        return result

