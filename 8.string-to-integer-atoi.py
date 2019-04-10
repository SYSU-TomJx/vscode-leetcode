#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (14.48%)
# Total Accepted:    328.2K
# Total Submissions: 2.3M
# Testcase Example:  '"42"'
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
#
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
# value is out of the range of representable values, INT_MAX (231 − 1) or
# INT_MIN (−231) is returned.
#
#
# Example 1:
#
#
# Input: "42"
# Output: 42
#
#
# Example 2:
#
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus
# sign.
# Then take as many numerical digits as possible, which gets 42.
#
#
# Example 3:
#
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a
# numerical digit.
#
#
# Example 4:
#
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a
# numerical
# digit or a +/- sign. Therefore no valid conversion could be performed.
#
# Example 5:
#
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed
# integer.
# Thefore INT_MIN (−231) is returned.
#
#
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = ['+', '-']
        nums = ['0','1','2','3','4','5','6','7','8','9']
        tmp_str = ''
        if str == '':
            return 0
        # Remove the whilespace in the front of str.
        if len(str) == 1 and str not in nums:
            return 0
        str = list(str)
        while(str[0] == ' '):
            str = list(str)
            del str[0]
            if len(str) == 0:
                return 0

        str = ''.join(str)

        for s in str:
            # Cut the string if not number or sign is met.
            if s not in sign+nums:
                break
            tmp_str = tmp_str + s
        # number or sign is not found at first position, return 0.
        if tmp_str == '':
            return 0
        # check the string when len is 1.
        if len(tmp_str) == 1:
            if tmp_str in nums:
                return int(tmp_str)
            return 0
        # check the filtting string is illegal.
        if tmp_str[0] == '+' and tmp_str[1] not in nums:
            return 0
        if tmp_str[0] == '-' and tmp_str[1] not in nums:
            return 0

        for i in range(len(tmp_str)):
            if i == 0 and tmp_str[i] in sign:
                continue
            if tmp_str[i] in nums:
                continue
            tmp_str = tmp_str[0:i]
            break

        res = int(tmp_str)
        bound_num = 2147483648
        if res >= 0:
            if res >= bound_num:
                res = bound_num-1
        else:
            if res < -bound_num:
                res = -bound_num
        return res

