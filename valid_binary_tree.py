# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def validate(root):

            if root == None or root.val ==0:
                return True
        
            if root.left and root.left.val >= root.val: 
                return False

            elif root.right and root.right.val <=  root.val:
                return False
    
            else:
                left = validate(root.left)
                right = validate(root.right)
                return left and right
        
        return validate(root)
        
