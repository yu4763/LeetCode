# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, root: TreeNode, level: int):
        if root == None:
            return level
        left = self.dfs(root.left, level+1)
        right = self.dfs(root.right, level+1)
        return max(left, right)