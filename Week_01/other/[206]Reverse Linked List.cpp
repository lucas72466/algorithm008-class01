/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL)
            return head;
        
        ListNode* pre = NULL;
        ListNode* cur = head;
        ListNode* tmp = NULL;
        while(cur!=NULL){
            ListNode* tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
};

/*
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        head = stack.pop()
        cur = head
        while len(stack):
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return head

*/