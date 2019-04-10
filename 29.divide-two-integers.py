#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.04%)
# Total Accepted:    181.4K
# Total Submissions: 1.1M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
#
# Note:
#
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 231 − 1 when the division
# result overflows.
#
#
#
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = dividend / divisor
        if res > 2147483647:
            return 2147483647
        if res < 0:
            if dividend % divisor != 0:
                res = res + 1
        if res < -2147483648:
            return -2147483648
        return res


