# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(root, subRoot):
            if root==None or subRoot ==None:
                return root==subRoot
            # print(root.val,subRoot.val)
            if root.val != subRoot.val:
                return False 
            return check(root.left, subRoot.left) and check(root.right, subRoot.right) 
    
        #traversing the main tree 
        def preorder(root):
            if root ==None:
                return False
            if root.val == subRoot.val:
                if check(root, subRoot):
                    return True 
                
            return preorder(root.left) or preorder(root.right)

        return preorder(root)
            
        

        