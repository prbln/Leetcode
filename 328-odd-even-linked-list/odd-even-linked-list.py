# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head 
        if not head.next:
            return head
        temp = head 
        evenHead = None 
        oddHead = None
        count = 1
        while(temp!=None):
            if count%2 ==0:
                if evenHead==None:
                    first = temp
                    evenHead = temp
                else:
                    prev.next = temp.next
                    evenHead.next = temp
                    evenHead = evenHead.next 
            else:
                if oddHead ==None:
                    start = temp
                    oddHead = temp
                else:
                    prev.next = temp.next
                    oddHead.next = temp
                    oddHead = oddHead.next 
            prev =  temp
            temp = temp.next 
            count+=1
        oddHead.next = first           
        return start
        