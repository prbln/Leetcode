# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = []
        q1 =[]
        def preorder(root, arr):
            if root ==None:
                arr.append(None)
                return None 
            arr.append(root.val)
            left = preorder(root.left, arr)
            right = preorder(root.right, arr)
        preorder(p, p1) 
        preorder(q, q1) 
        # print(q1,p1)
        if p1 ==q1:
            return True
        else:
            return False 

            
