# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        ## create recursive function

        def valid(node, left, right):
            if not node:
                return True
            
            # if the node val is not between left and right returns false
            if not (node.val < right and node.val > left):
                return False
            
            ## when validating left tree, change left upper limit to the value fo the previous node.
            ## when validating right tree, change the lower limit to the value of the previous node.
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
            
            
        return valid(root, float ("-inf"), float("inf"))
        
        
        
