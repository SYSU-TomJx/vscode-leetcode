#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (49.70%)
# Total Accepted:    204.4K
# Total Submissions: 410.8K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: 3
# Output: "III"
#
# Example 2:
#
#
# Input: 4
# Output: "IV"
#
# Example 3:
#
#
# Input: 9
# Output: "IX"
#
# Example 4:
#
#
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
#
# Example 5:
#
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tbl = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        num_lst = []
        while num != 0:
            tmp = num % 10
            num_lst.append(tmp)
            num = num / 10
        x = 1
        res = []
        for num in num_lst:
            if num >3 and num <9:
                key_1 = 5
            else:
                key_1 = 1
            prim_key = key_1 * x
            prim_val = tbl[prim_key]
            minor_val = tbl[x] # I, X, C, M
            tmp_str = ''
            cmp_key = num
            if cmp_key==4 or cmp_key==9:
                if cmp_key == 9:
                    prim_val = tbl[prim_key*10]
                tmp_str = minor_val + prim_val # minor, primal
            elif cmp_key<=3:
                for i in range(cmp_key):
                    tmp_str = tmp_str + minor_val # primal, primal, primal

            elif cmp_key>5 and cmp_key<=8:
                # primal, minor,...
                tmp_str =  prim_val
                for i in range(cmp_key-5):
                    tmp_str = tmp_str + minor_val
            elif cmp_key == 5:
                tmp_str = prim_val
            res.append(tmp_str)
            x = x * 10
        res = res[::-1]
        res = ''.join(res)
        return res




