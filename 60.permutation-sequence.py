#
# @lc app=leetcode id=60 lang=python
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (32.33%)
# Total Accepted:    129.9K
# Total Submissions: 401.6K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# Given n and k, return the k^th permutation sequence.
#
# Note:
#
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#
#
'''
class Solution(object):
    def solver(self, nums, size, k, seq_set, seq, cnt,sw):
        if len(seq) == size:
            cnt[0] += 1
            if cnt[0] == k:
                seq_set.append(seq)
                sw[0] = False
                return
        if sw[0] == True:
            for i in range(len(nums)):

                res = self.solver(nums[:i]+nums[i+1:], size, k, seq_set, seq+nums[i], cnt, sw)
                if res is True:
                    break
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = ''
        # create the first permutation.
        for s in range(1,n+1):
            nums += str(s)
        res_set = []
        cnt = [0]
        sw = [True]
        #DFS
        self.solver(nums,n,k, res_set,'',cnt,sw)
        return res_set[0]
'''
class Solution(object):
    def get_factorial(self, n):
        res = 1
        if n == 0:
            return 1 # 0! = 1
        for i in range(1, n+1):
            res *= i
        return res
    def getPermutation(self, n, k):
        """
        Reference:
        https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        k -= 1
        cnt = 1
        init_set = []
        for i in range(1,n+1):
            init_set.append(str(i))
        while len(res) != n:
            factorial = self.get_factorial(n-cnt)
            ids = k / factorial
            res += init_set[ids]
            init_set.pop(ids)
            k = k - ids * factorial
            cnt += 1
        return res


