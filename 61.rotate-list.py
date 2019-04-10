#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (26.53%)
# Total Accepted:    180.6K
# Total Submissions: 678.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
#
#
# Example 2:
#
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head == None:
            return head
        val_set = []
        head_node = ListNode(None)
        head_node.next = head
        cur_node = head
        while cur_node != None:
            val_set.append(cur_node.val)
            cur_node = cur_node.next
        k = k % len(val_set)
        val_set = val_set[::-1][0:k][::-1] + val_set[0:len(val_set)-k]
        cur_node = head_node.next
        cnt = 0
        while cur_node != None:
            cur_node.val = val_set[cnt]
            cnt = cnt + 1
            cur_node = cur_node.next
        head_node = head_node.next
        return head_node
'''
class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head == None or head.next==None:
            return head
        val_set = []
        head_node = ListNode(None)
        head_node.next = head
        lst_len = 0
        while head != None:
            lst_len = lst_len + 1
            head = head.next
        k = k % lst_len
        if k == 0:
            head_node = head_node.next
            return head_node
        slow_node = head_node.next
        fast_node = head_node.next
        tmp_k = [k][0]
        while tmp_k > 0:
            fast_node = fast_node.next
            tmp_k = tmp_k - 1
        while fast_node.next != None:
            fast_node = fast_node.next
            slow_node = slow_node.next

        fast_node.next = head_node.next
        head_node.next = slow_node.next
        slow_node.next = None
        head_node = head_node.next
        return head_node


