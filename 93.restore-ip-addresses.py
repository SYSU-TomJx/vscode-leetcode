#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (31.05%)
# Total Accepted:    134.4K
# Total Submissions: 432.9K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
#
# Example:
#
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
#
#
#
class Solution(object):
    def solver(self, s, idx, path, res):
        if idx == 4:
            if not s:
                res.append(path[:-1])
            return
        for i in range(1,4):
            if i <= len(s):
                if i == 1:
                    self.solver(s[i:], idx+1, path+s[:i]+'.', res)
                elif i == 2 and s[0] != '0':
                    self.solver(s[i:], idx+1, path+s[:i]+'.', res)
                elif i == 3 and s[0] != '0' and int(s[:i]) <= 255:
                    self.solver(s[i:], idx+1, path+s[:i]+'.', res)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.solver(s, 0, '', res)
        return res


