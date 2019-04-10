#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (29.99%)
# Total Accepted:    185.2K
# Total Submissions: 617.4K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Example 1:
#
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Note:
#
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
#
#
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1] # Calculate the result from the rear.
        num2 = num2[::-1]
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) < len(num2):
            row_len = len(num1) + 1
            row_num = num1
            col_len = len(num2) + 1
            col_num =num2
        else:
            row_len = len(num2) + 1
            row_num = num2
            col_len = len(num1) + 1
            col_num = num1
        num_mat = []
        for row in range(row_len):
            num_mat.append([0]*col_len)
        adv = 0
        # store the multiply results between each nums in a matrix.
        tmp_ad = []
        for row in range(row_len):
            if row == row_len - 1:
                break
            for col in range(col_len):
                if col == col_len - 1:
                    num_mat[row][col] = adv # store the adv at the last column.
                    adv = 0
                    break
                mul_res = int(row_num[row]) * int(col_num[col]) + adv
                adv = mul_res / 10
                num_mat[row][col] = mul_res % 10
                tmp_ad.append(adv)
        res = ''

        for col in range(0, col_len):
            row = 0
            col1 = col
            tmp_res = 0

            while row<row_len and col1>=0:
                tmp_res += num_mat[row][col1]
                row += 1
                col1 -= 1
            tmp_res = tmp_res + adv
            res = str(tmp_res%10) + res
            adv = tmp_res / 10

        row = 1
        while row < row_len:
            col = col_len - 1
            row1 = row
            tmp_res = 0
            while row1<row_len and col>0:
                tmp_res += num_mat[row1][col]
                row1 += 1
                col -= 1
            tmp_res = tmp_res + adv
            res = str(tmp_res%10) + res
            adv = tmp_res / 10
            row += 1
        while res[0] == '0':
            res = res[1:]
        if adv != 0:
            res = str(adv) + res
        return res
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1] # Calculate the result from the rear.
        num2 = num2[::-1]
        product = [0] * (len(num1)+len(num2))
        pos = 1
        for n1 in num1:
            tmp_pos = pos
            for n2 in num2:
                product[tmp_pos-1] += int(n1)*int(n2)
                product[tmp_pos] += product[tmp_pos-1] / 10
                product[tmp_pos-1] %= 10
                tmp_pos += 1
            pos += 1
        product = product[::-1]
        while product[0]==0 and len(product)!=1:
            product = product[1:]
        product = [str(x) for x in product]
        return ''.join(product)
