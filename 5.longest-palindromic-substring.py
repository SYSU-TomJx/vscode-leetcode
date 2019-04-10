#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.52%)
# Total Accepted:    480.1K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        max_s = ''
        rev_s = s[::-1]
        if rev_s == s:
            return s
        #s_mat = []
        pali_mat_1 = []
        #pali_mat_2 = []
        max_sub_len = 0
        # Create the LCS matrix
        for i in range(s_len+1):
            #arr_col = []
            arr_col_p = []
            for j in range(s_len+1):
                #arr_col.append(0)
                arr_col_p.append('')
            #s_mat.append(arr_col)
            pali_mat_1.append(arr_col_p)
            #pali_mat_2.append(arr_col)
            for j in range(s_len+1):
                if i>0 and j>0:
                    if s[j-1] == rev_s[i-1]:
                        #s_mat[i][j] = s_mat[i-1][j-1] + 1
                        pali_mat_1[i][j] = pali_mat_1[i-1][j-1] +\
                                           pali_mat_1[i][j] + rev_s[i-1]
                        sub_s = pali_mat_1[i][j]
                        pali_mat_1[i-1][j-1] = None
                        rev_sub_s = sub_s[::-1]
                        sub_s_len = len(sub_s)
                        if rev_sub_s == sub_s:
                            #pali_mat_2[i][j] = 1
                            if sub_s_len > max_sub_len:
                                max_sub_len = sub_s_len
                                max_s = sub_s

        return max_s
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        max_s = ''
        rev_s = s[::-1]
        if rev_s == s:
            return s
        max_s = ''
        for i in range(s_len):
            j = i + 1
            while j <= s_len and len(s[i:j])<= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= len(max_s):
                    max_s = s[i:j]
                j = j + 1
        return max_s
'''
