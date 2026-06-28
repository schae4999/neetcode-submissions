# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0

        def dfs(node):
            nonlocal idx

            if not node:
                return None

            left = dfs(node.left)
            if left is not None:
                return left

            idx += 1

            if idx == k:
                return node.val

            right = dfs(node.right)
            if right is not None:
                return right

            return None

        return dfs(root)