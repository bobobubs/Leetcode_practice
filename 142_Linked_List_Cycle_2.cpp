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
    ListNode *detectCycle(ListNode *head) {
        //map to store address of nodes already visitied
        unordered_map<ListNode*, int> m;
        
        //traverse the list
        while(head){
            
            //if the node already exists in the map
            if(m.count(head)){
                return head;
            }
            //otherwise add to map and continue
            m[head] = head->val;
            head = head->next;
        }
        return nullptr;
    }
};
