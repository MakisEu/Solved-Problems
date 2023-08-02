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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int r=0,sum=0,tempp;
        vector<int> sums;
        ListNode *Next1=l1;
        ListNode *Next2=l2;
        int t1=0,t2=0;
        while (Next1!=nullptr || Next2!=nullptr)
        {
            t1=0;
            t2=0;
            if (Next1!=nullptr){
                t1=Next1->val;
                Next1=Next1->next;
            }
            if (Next2!=nullptr){
                t2=Next2->val;
                Next2=Next2->next;
            }
            tempp=t1+t2+r;
            r=tempp/10;
            sums.push_back(tempp%10);
        }
        tempp=0;
        bool flag=true;
        ListNode *temp,*start=new ListNode();
        if (r>0){
            start=new ListNode(r);
            flag=false;
        }
        for (int i=sums.size()-1;i>-1;i--){
            
            if (flag){
                flag=false;
                start=new ListNode(sums[i]);
            }
            else{
            start=new ListNode(sums[i],start);}
        }
        return start;
        
    }
};
