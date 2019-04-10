#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (43.04%)
# Total Accepted:    284K
# Total Submissions: 656.5K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        head_node = ListNode(None)
        head_node.next = head
        pre = head_node
        tail = head.next
        cnt = 0
        while tail != None:
            if cnt % 2 == 0:
                tmp = pre.next
                tmp.next = tail.next
                tail.next = tmp
                pre.next = tail
                tail = tmp
            pre = pre.next
            tail = tail.next
            cnt += 1
        head_node = head_node.next
        return head_node

