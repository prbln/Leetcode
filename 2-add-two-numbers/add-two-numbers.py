# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = 0 
        head = ListNode()
        temp = head
        while(l1 or l2):
            num1, num2 = 0, 0 
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            temp.val = (num1 +num2 + carryOver ) %10 
            carryOver = (num1 +num2 +carryOver ) // 10
            temp.next = ListNode()
            prev = temp
            temp = temp.next
        if carryOver !=0:
            temp.val = carryOver
            temp.next = None
        else : 
            prev.next = None
        return head
    
            