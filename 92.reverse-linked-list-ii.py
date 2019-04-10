#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (34.46%)
# Total Accepted:    186.2K
# Total Submissions: 540.2K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        margin = n-m
        pre = head_node = ListNode(None)
        head_node.next = head

        #pre = head_node
        cnt = 0
        while cnt < m-1:
            pre = pre.next
            head = head.next
            cnt += 1
        while margin > 0:
            # cut the node
            tmp_node = head.next
            head.next = tmp_node.next

            # insert
            tmp_node.next = pre.next
            pre.next = tmp_node

            margin -= 1

        head_node = head_node.next
        #head_node.val = margin
        return head_node
