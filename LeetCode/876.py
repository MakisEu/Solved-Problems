# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        node=head
        if (node==None):
            return head
        n=0
        while (node!=None):
            node=node.next
            n+=1
        middle=n//2
        node=head
        for i in range(middle):
            node=node.next
        return node
