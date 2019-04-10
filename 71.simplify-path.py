#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (28.16%)
# Total Accepted:    143K
# Total Submissions: 506.2K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it. Or in other
# words, convert it to the canonical path.
#
# In a UNIX-style file system, a period . refers to the current directory.
# Furthermore, a double period .. moves the directory up a level. For more
# information, see: Absolute path vs relative path in Linux/Unix
#
# Note that the returned canonical path must always begin with a slash /, and
# there must be only a single slash / between two directory names. The last
# directory name (if it exists) must not end with a trailing /. Also, the
# canonical path must be the shortest string representing the absolute
# path.
#
#
#
# Example 1:
#
#
# Input: "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
#
#
# Example 2:
#
#
# Input: "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
#
#
# Example 3:
#
#
# Input: "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
#
#
# Example 4:
#
#
# Input: "/a/./b/../../c/"
# Output: "/c"
#
#
# Example 5:
#
#
# Input: "/a/../../b/../c//.//"
# Output: "/c"
#
#
# Example 6:
#
#
# Input: "/a//b////c/d//././/.."
# Output: "/a/b/c"
#
#
#
class Solution(object):
    '''
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # "/a//b////c/d//././/.." to [a,b,c,d,.,.,..]
        path_list = []
        content = ''
        for c in path:
            if c == '/':
                if content != '':
                    path_list.append(content)
                content = ''
            else:
                content = content + c
        if content != '':
            path_list.append(content)
        new_path_list = []
        for c in path_list:
            if c == '..':
                if new_path_list != []:
                    new_path_list = new_path_list[0:-1]
            elif c == '.':
                continue
            else:
                new_path_list.append(c)
        if new_path_list == []:
            return '/'
        res_path = ''
        for item in new_path_list:
            res_path = res_path + '/'+ item
        return res_path
    '''
    def simplifyPath(self, path):
        path_list = path.split('/')
        res_path = []
        for item in path_list:
            if item in ('','.'):
                continue
            elif item == '..':
                if res_path != []:
                    res_path.pop()
            else:
                res_path.append(item)
        return '/'+'/'.join(res_path)







