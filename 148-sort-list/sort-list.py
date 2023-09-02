# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeTwoSortedArray(list1, list2):
            temp1 = list1
            temp2 = list2
            if temp1 ==None:
                return temp2
            if temp2 == None:
                return temp1
            if temp1.val <temp2.val:
                res = temp1
                temp1 = temp1.next
            else:
                res = temp2
                temp2 = temp2.next
            ptr = res
            while(temp1!= None and  temp2!= None):
                if temp1.val<= temp2.val:
                    ptr.next = temp1
                    ptr = temp1 
                    temp1 = temp1.next
                else:
                    ptr.next = temp2 
                    ptr = temp2 
                    temp2= temp2.next
            if temp1 == None:
                ptr.next = temp2
            elif temp2 == None:
                ptr.next = temp1
            return res
        def mergeSort(head):
            if not head:
                return None 
            if head.next == None:
                return head 
            slow = head
            fast = head 
            while(fast and fast.next):
                prev = slow
                slow = slow.next 
                fast = fast.next 
                fast = fast.next
            
            prev.next = None
            left =  mergeSort(head) 
            right = mergeSort(slow) 
            
            
            # print(right.val, left.val)
            x = mergeTwoSortedArray(left, right)
            # print(x.val)
            return x
        return mergeSort(head)
            
