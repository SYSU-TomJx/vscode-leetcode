#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.54%)
# Total Accepted:    764K
# Total Submissions: 2.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_list(self, lst):
        '''
        Reverse the given list.
        '''
        end = lst
        head = ListNode(end.val)
        end = end.next
        while end is not None:
            tmp = ListNode(end.val)
            tmp.next = head
            head = tmp
            end = end.next
        return head

    def addTwoNumbers(self, l1, l2):
        l3_head = ListNode(None)
        l3 = ListNode(0)
        l3_head.next = l3
        pre = l3
        # Reverge the input number list
        #l1 = self.reverse_list(l1)
        #l2 = self.reverse_list(l2)

        # Trival l1&l2, create a new list to saving the sum of l1&l2.

        l1_end = l1
        l2_end = l2
        while l1_end is not None and l2_end is not None:
            sum_res = l1_end.val + l2_end.val + l3.val
            l3.val = sum_res % 10
            end = ListNode(sum_res/10)
            l1_end = l1_end.next
            l2_end = l2_end.next
            pre = l3
            l3.next = end
            l3 = end

        retail_lst = None
        if l2_end is None:
            retail_lst = l1_end

        elif l1_end is None:
            retail_lst = l2_end

        if retail_lst is None:
            if l3.val == 0:
                pre.next = None
                l3 = None
            return l3_head.next

        while retail_lst is not None:
            sum_res = l3.val + retail_lst.val
            l3.val = sum_res % 10
            end = ListNode(sum_res/10)
            retail_lst = retail_lst.next
            pre = l3
            l3.next = end
            l3 = end
        if l3.val == 0:
            l3 = None
            pre.next = None
        return l3_head.next

