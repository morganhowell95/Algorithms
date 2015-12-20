/*
Add Two Numbers
Caleb
This can be prettier
*/
/*You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *list = NULL;
    struct ListNode *head = NULL;
    int carry = 0;
    
    if (!l1 && !l2) {
        return NULL;
    }
    else {
        int sum = l1->val + l2->val + carry;
        if (sum >= 10) {
            carry = sum / 10;
            sum = sum % 10;
        }
        else {
            carry = 0;
        }
        list = malloc(sizeof(struct ListNode));
        list->val = sum;
        list->next = NULL;
        head = list;
        l1 = l1->next;
        l2 = l2->next;
    }
    
    while (l1 && l2) {
        int sum = l1->val + l2->val + carry;
        if (sum >= 10) {
            carry = sum / 10;
            sum = sum % 10;
        }
        else {
            carry = 0;
        }
        struct ListNode *newNode = malloc(sizeof(struct ListNode));
        newNode->val = sum;
        newNode->next = NULL;
        list->next = newNode;
        list = list->next;

        l1 = l1->next;
        l2 = l2->next;
    }
    
    if (l1) {
        if (!list) {
            list = malloc(sizeof(struct ListNode));
            list->val = l1->val;
            list->next = NULL;
            head = list;
            l1 = l1->next;
        }
        while (l1) {
            int sum = l1->val + carry;
            if (sum >= 10) {
                carry = sum / 10;
                sum = sum % 10;
            }
            else {
                carry = 0;
            }
            struct ListNode *newNode = malloc(sizeof(struct ListNode));
            newNode->val = sum;
            newNode->next = NULL;
            list->next = newNode;
            list = list->next;
            l1 = l1->next;
        }
    }
    else if (l2) {
        if (!list) {
            list = malloc(sizeof(struct ListNode));
            list->val = l2->val;
            list->next = NULL;
            head = list;
            l2 = l2->next;
        }
        while (l2) {
            int sum = l2->val + carry;
            if (sum >= 10) {
                carry = sum / 10;
                sum = sum % 10;
            }
            else {
                carry = 0;
            }
            struct ListNode *newNode = malloc(sizeof(struct ListNode));
            newNode->val = sum;
            newNode->next = NULL;
            list->next = newNode;
            list = list->next;
            l2 = l2->next;
        }
    }
    
    if (carry > 0) {
        struct ListNode *newNode = malloc(sizeof(struct ListNode));
        newNode->val = carry;
        newNode->next = NULL;
        list->next = newNode;
        list = list->next;
    }
    
    return head;
}