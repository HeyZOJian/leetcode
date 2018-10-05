/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
  public:
    ListNode *middleNode(ListNode *head)
    {
        int len = 0;
        ListNode *headCopy = head;
        while (headCopy->next != NULL)
        {
            len++;
            headCopy = headCopy->next;
        }
        if (len % 2 == 0)
            len = len / 2;
        else
            len = len / 2 + 1;
        while (len > 0)
        {
            head = head->next;
            len--;
        }
        return head;
    }
};