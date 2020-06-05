Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.
left has a value < node.val, and any descendant of node.right has a value > node.val.  
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

https://assets.leetcode.com/uploads/2019/03/06/1266.png

python solution:

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
        

