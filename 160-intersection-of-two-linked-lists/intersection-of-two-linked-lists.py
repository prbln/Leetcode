# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tailA = headA
        tailB = headB
        hashmap = dict()
        while(tailA!=None):
            hashmap[tailA] = True 
            tailA = tailA.next
        while(tailB!=None):
            if  hashmap.get(tailB, False):
                return tailB
            else:
                tailB = tailB.next
        return None



        