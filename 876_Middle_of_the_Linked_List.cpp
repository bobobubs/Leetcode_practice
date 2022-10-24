/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int numNodes = 0;
        //count the number of the nodes in the linked list
        ListNode *copy = head;
        while(head){
            head = head->next;
            numNodes++;
        }
        //find the value of the middle node
        int middleNode = (numNodes /2);
        cout << middleNode << endl;
        //traverse to the middle node
        while(middleNode!=0){
            copy = copy->next;
            middleNode += -1;
        }
        return copy;
    }
};
