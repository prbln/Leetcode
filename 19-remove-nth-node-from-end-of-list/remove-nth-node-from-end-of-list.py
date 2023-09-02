# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        temp = head
        while(temp!= None):
            leng+=1  
            temp = temp.next 
        if leng <=2:
            fromStart = leng - n
            if fromStart ==0:
                return head.next 
            else:
                head.next = None 
                return head
                
        fromStart = leng - n
        if fromStart==0 :
            return head.next
        prev = head 
        while(fromStart-1>0):
            prev = prev.next 
            fromStart-=1


        if prev.next.next:
            prev.next = prev.next.next 
        else:
            prev.next = None
        return head
        


