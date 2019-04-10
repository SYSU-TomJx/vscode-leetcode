#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (32.36%)
# Total Accepted:    172K
# Total Submissions: 531.2K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        head_node = ListNode(None)
        head_node.next = head
        lst_dict = {}
        lst_arr = []
        while head != None:
            if head.val not in lst_dict.keys():
                lst_dict[head.val] = 1
                lst_arr.append(head.val)
            else:
                lst_dict[head.val] = lst_dict[head.val] + 1
            head = head.next

        new_head = ListNode(None)
        tr_node = new_head
        for k in lst_arr:
            if lst_dict[k] > 1:
                continue
            tmp_node = ListNode(k)
            tr_node.next = tmp_node
            tr_node = tr_node.next
        new_head = new_head.next
        return new_head
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        head_node = ListNode(None)
        head_node.next = head
        pre = head_node
        while head and head.next !=None:
            if head.val == head.next.val:
                while head and head.next!=None and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        head_node = head_node.next
        return head_node
