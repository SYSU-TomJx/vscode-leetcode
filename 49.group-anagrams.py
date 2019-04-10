#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (44.88%)
# Total Accepted:    300.2K
# Total Submissions: 668.2K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note:
#
#
# All inputs will be in lowercase.
# The order of your output does not matter.
#
#
#
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sort_strs = []
        res = []
        for s in strs:
            tmp = list(s)
            tmp.sort()
            tmp = ''.join(tmp)
            sort_strs.append(tmp)
        visited = []
        for i in range(len(strs)):
            if sort_strs[i] in visited:
                continue
            visited.append(sort_strs[i])
            anagram = [strs[i]]
            for j in range(i+1, len(strs)):
                if sort_strs[j] == sort_strs[i]:
                    anagram.append(strs[j])
            res.append(anagram)
        return res
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # get the counts of each str in strs
        sort_strs = []
        tbl = {}
        for s in strs:
            tmp = sorted(s)
            tmp = ''.join(tmp)
            sort_strs.append(tmp)
        for i, s in enumerate(sort_strs):
            if s not in tbl:
                tbl[s] = [strs[i]]
            else:
                tbl[s].append(strs[i])
        res = tbl.values()
        return res

