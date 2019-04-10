#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (33.96%)
# Total Accepted:    357.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
#
# Example:
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
#
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lst_len = 0
        head_node = ListNode(None)
        head_node.next = head
        tail = head
        while tail != None:
            tail = tail.next
            lst_len += 1
        if n > lst_len:
            head_node = head_node.next
            return head_node
        pos = lst_len - n
        cnt = 0
        tail = head_node.next
        pre = head_node
        while cnt < pos:
            pre = tail
            tail = tail.next
            cnt += 1
        pre.next = tail.next
        head_node = head_node.next
        return head_node




