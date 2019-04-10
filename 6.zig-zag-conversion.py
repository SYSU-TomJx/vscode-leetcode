#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (30.60%)
# Total Accepted:    287.8K
# Total Submissions: 938.2Kw
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_mat = []
        s_len = len(s)
        if numRows <= 1:
            return s
        header = 0
        header_1 = numRows
        diag_nums = numRows - 2
        while header < s_len:
            arr_col_1 = ['']*numRows
            arr_col_2 = ['']*numRows
            tmp_dim = diag_nums

            while tmp_dim > 0:
                if header_1-1+tmp_dim >= s_len:
                    tmp_dim = tmp_dim - 1
                    continue
                arr_col_2[diag_nums-tmp_dim+1] = s[header_1+tmp_dim-1]
                tmp_dim = tmp_dim - 1
            #arr_col_2 = arr_col_2[::-1]

            for i in range(numRows):
                if header+i >=s_len:
                    break
                arr_col_1[i] = s[header+i]

            str_mat.append(arr_col_1)
            str_mat.append(arr_col_2)
            header = header_1 + diag_nums
            header_1 = header + numRows
        res_str = ''
        for col in range(len(str_mat[0])):
            for row in range(len(str_mat)):
                res_str = res_str + str_mat[row][col]

        return res_str

