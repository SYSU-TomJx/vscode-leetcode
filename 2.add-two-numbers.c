/*
 * @lc app=leetcode id=2 lang=c
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (30.54%)
 * Total Accepted:    764K
 * Total Submissions: 2.5M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 *
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 *
 * Example:
 *
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 *
 *
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reverse_list(struct ListNode* lst){
    ListNode *head = lst;
    ListNode *end = lst;
    while(end->next != NULL){
        ListNode* tmp = end->next;
        end->next = tmp->next;
        tmp->next = head;
        head = tmp;
    }
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // reverse the given listes.
    reverse_list(l1);
    reverse_list(l2);
    ListNode* l1_node = l1;
    ListNode* l2_node = l2;
    ListNode* sum_lst = new ListNode();
    sum_lst->val = 0;
    sum_lst->next = NULL;
    ListNode* sum_node = sum_lst;

    while(l1_node != NULL && l2_node != NULL){
        int sum_val = l1_node->val + l2_node->val;
        int pos1_val = sum_val % 10;
        int pos2_val = sum_val / 10;
        sum_node->val = pos1_val;
        ListNode* tmp_node = new ListNode();
        tmp_node->val = pos2_val;
        tmp_node->next = sum_node;
        sum_node = tmp_node;

        l1_node = l1_node->next;
        l2_node = l2_node->next;
    }
    ListNode* retail = NULL;
    if (l1_node == NULL){
        retail = l2_node;
    }
    else if (l2_node == NULL){
        retail = l1_node;
    }
    else{
        if(sum_node->val == 0){
            sum_node = sum_node->next;
        }
        return sum_node;
    }

    while(retail != NULL){
        int sum_val = sum_node->val + retail->val;
        int pos1_val = sum_val % 10;
        int pos2_val = sum_val / 10;

        sum_node->val = pos1_val;
        ListNode* tmp_node = new ListNode();
        tmp_node->val = pos2_val;
        tmp_node->next = sum_node;
        sum_node = tmp_node;

        retail = retail->next;
    }

    if (sum_node->val == 0){
        sum_node = sum_node->next;
    }
    return sum_node;
}

