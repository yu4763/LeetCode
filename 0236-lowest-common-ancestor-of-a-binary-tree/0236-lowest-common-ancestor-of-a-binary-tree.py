# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []
        self.dfs(root, p, q, res)
        return res[0]

    def dfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', res: list):

        if root == None:
            return False, False
            
        found_p = False
        found_q = False
        if root == p:
            found_p = True
        if root == q:
            found_q = True
        
        
        p1, q1 = self.dfs(root.left, p, q, res)
        p2, q2 = self.dfs(root.right, p, q, res)
        
        result_p = found_p or p1 or p2
        result_q = found_q or q1 or q2

        if result_p and result_q:
            res.append(root)
        
        return (result_p, result_q)