#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (36.74%)
# Total Accepted:    157.9K
# Total Submissions: 429.8K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head_node = ListNode(None)
        head_node_2 = ListNode(None)
        pre_low = head_node_2
        pre_high = head_node
        while head != None:
            tmp = ListNode(head.val)
            if head.val < x:
                pre_low.next = tmp
                pre_low = tmp
            else:
                pre_high.next = tmp
                pre_high = tmp
            head = head.next
        head_node = head_node.next
        pre_low.next = head_node
        head_node_2 = head_node_2.next
        return head_node_2






