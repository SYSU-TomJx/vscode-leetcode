#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.63%)
# Total Accepted:    212.7K
# Total Submissions: 715.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_mat = []
        s_mat = []
        arr_res = []
        s_len = len(nums)
        # sort the nums
        nums.sort()
        # create a matrix, each elem denotes the sum of 2 numbers.
        sum_mat = []
        arr_col = [0]*s_len
        for i in range(s_len):
            j = i + 1
            while j < s_len:
                arr_col[j] = nums[i] + nums[j]
                j = j + 1
            if i < s_len-1:
                s_mat.append(arr_col)
                arr_col = [0]*s_len

        # trival the matrix and find the sum of 4 elems that equal to target number.
        for row in range(s_len-1):
            col = row + 1
            if col == s_len - 1:
                break
            while col < s_len - 1 and s_mat[row][col] == s_mat[row][col+1]:
                col = col + 1

            header = [row, col]
            tail = [s_len-2, s_len-1]
            arr_res.append([header, tail])
            while header[0] < tail[0] and header[1]<s_len-1:
                #while header[1] + 1 < s_len-1 and s_mat[header[0]][header[1]+1] == s_mat[header[0]][header[1]]:
                #    header[1] += 1
                part_1 = s_mat[header[0]][header[1]]
                part_2 = s_mat[tail[0]][tail[1]]
                tmp_res = part_1 + part_2
                if tmp_res < target:
                    header[1] += 1
                    if header[1] == tail[0]:
                        header[1] += 1
                elif tmp_res > target:
                    if tail[1]-1 > tail[0]:
                        if tail[1]-1 == header[0]:
                            tail[0] -= tail[0]

                else:
                    tmp_arr = [nums[header[0]], nums[header[1]], nums[tail[0]], nums[tail[1]]]
                    tmp_arr.sort()
                    if tmp_arr not in result_mat:
                        result_mat.append(tmp_arr)

                    header[1] += 1
                    #tail[0] -= 1



        return arr_res


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_mat = []
        s_mat = []
        arr_res = []
        s_len = len(nums)
        # sort the nums
        nums.sort()
        # create a matrix, each elem denotes the sum of 2 numbers.
        sum_mat = []
        arr_col = [0]*s_len
        for i in range(s_len):
            j = i + 1
            while j < s_len:
                arr_col[j] = nums[i] + nums[j]
                j = j + 1
            if i < s_len-1:
                s_mat.append(arr_col)
                arr_col = [0]*s_len

        # trival the matrix and find the sum of 4 elems that equal to target number.
        for row in range(s_len-1):
            col = row + 1
            if col == s_len - 1:
                break
            # first loop
            while col < s_len:
                row_2 = row + 1
                # second loop
                while row_2 < s_len-1:
                    # thrid loop
                    col_2 = row_2 + 1
                    while col_2 < s_len:
                        if col_2 == col or row == col_2 or row_2 == col:
                            col_2 += 1
                            continue
                        tmp_sum = s_mat[row][col] + s_mat[row_2][col_2]
                        if tmp_sum == target:
                            tmp_arr = [nums[row], nums[col], nums[row_2], nums[col_2]]
                            tmp_arr.sort()
                            if tmp_arr not in result_mat:
                                result_mat.append(tmp_arr)
                        col_2 += 1
                    row_2 += 1
                col += 1
        return result_mat
    '''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_mat = []
        s_mat = []
        arr_res = []
        s_len = len(nums)
        # sort the nums
        nums.sort()
        # create a matrix, each elem denotes the sum of 2 numbers.
        sum_mat = []
        arr_col = [0]*s_len
        for i in range(s_len):
            j = i + 1
            while j < s_len:
                arr_col[j] = nums[i] + nums[j]
                j = j + 1
            if i < s_len-1:
                s_mat.append(arr_col)
                arr_col = [0]*s_len

        # trival the matrix and find the sum of 4 elems that equal to target number.
        for row in range(s_len-1):
            col = row + 1
            while col < s_len:
                row_1 = row + 1
                col_1 = col + 1
                header = s_mat[row][col]
                if col-1==row:
                    tail = s_mat[row+1][col+1]
                else:
                    left = header + s_mat[row+1][col-1]
                    right = header + s_mat[row+1][col+1]
                    left_res = max(left, target) - min(left, target)
                    right_res = max(right, target) - min(right, target)
                    if left_res < right:
                        tail = left
                        col_1 = col - 1
                    else:
                        tail = right
                sw = True
                while sw:
                    tmp_tail_left = None
                    tmp_tail_right = None
                    tmp_tail_down = None
                    if col_1 < col:

                        if col_1 - 1 != row_1:
                            tmp_tail_left = s_mat[row_1][col_1-1]
                        if row_1 + 1 != col_1:
                            tmp_tail_down = s_mat[row_1+1][col_1]
                        if tmp_tail_left!=None and tmp_tail_down!=None:
                            # calculate the margin
                            left_res = max(tmp_tail_left, target) - min(tmp_tail_left, target)
                            down_res = max(tmp_tail_down, target) - min(tmp_tail_down, target)

                            if left_res == 0:
                                result_mat.append(nums[row], nums[col], nums[row_1], nums[col-1])
                            elif down_res == 0:
                                result_mat.append(nums[row], nums[col], nums[row_1+1], nums[col_1])

                            if left_res < right_res:
                                tail = tmp_tail_left
                                col_1 -= 1
                            else:
                                tail = tmp_tail_down
                                row_1 += 1


                        elif tmp_tail_left is None and tmp_tail_down!=None:
                            tail = tmp_tail_down
                        elif tmp_tail_left!=None and tmp_tail_down is None:
                            tail = tmp_tail_left
                        else:
                            sw = False
                    else:
                        if col_1 + 1 != s_len:
                            tmp_tail_right = s_mat[row_1][col_1+1]
                        if row_1 + 1 != s_len - 1:
                            tmp_tail_down = s_mat[row_1+1][col_1]

                        if tmp_tail_left!=None and tmp_tail_down!=None:
                            # calculate the margin
                            right_res = max(tmp_tail_right, target) - min(tmp_tail_right, target)
                            down_res = max(tmp_tail_down, target) - min(tmp_tail_down, target)

                            if right_res == 0:
                                result_mat.append(nums[row], nums[col], nums[row_1], nums[col+1])
                            elif down_res == 0:
                                result_mat.append(nums[row], nums[col], nums[row_1+1], nums[col_1])

                            if right_res < down_res:
                                tail = tmp_tail_right
                                col_1 += 1
                            else:
                                tail = tmp_tail_down
                                row_1 += 1


                        elif tmp_tail_right is None and tmp_tail_down!=None:
                            tail = tmp_tail_down
                        elif tmp_tail_right!=None and tmp_tail_down is None:
                            tail = tmp_tail_right
                        else:
                            sw = False
        return result_mat


