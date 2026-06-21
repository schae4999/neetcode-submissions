# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.iterate(p) == self.iterate(q)
        
    def iterate(self, root):
        if not root:
            return [None]

        left = self.iterate(root.left)
        right = self.iterate(root.right)

        return [root.val] + left + right