#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (30.58%)
# Total Accepted:    258.5K
# Total Submissions: 845.3K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
#
class Solution(object):
    def solver(self, board, word, row, col):
        if word == '':
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or word[0] != board[row][col]:
            return False
        board[row][col] = '#'
        res = self.solver(board, word[1:], row+1, col) or\
        self.solver(board,word[1:],row-1, col) or\
        self.solver(board,word[1:],row, col+1) or\
        self.solver(board,word[1:],row, col-1)

        board[row][col] = word[0]
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        c_nums = row*col
        for i in range(c_nums):
            if self.solver(board, word, i/col, i%col):
                return True
        return False



