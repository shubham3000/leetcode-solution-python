
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def insert(root,val):
            if not root:
                return TreeNode(val)
            elif (val<root.val):
                root.left=insert(root.left,val)
            else:
                root.right=insert(root.right,val)
            return root
        
        output=None
        for i in preorder:
            output=insert(output,i)
        
        return output
        

