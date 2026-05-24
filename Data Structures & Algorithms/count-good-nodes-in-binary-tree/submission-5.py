# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxVal):
            nonlocal res
            if not node: return 0
            if node.val >= maxVal:
                res += 1
            maxVal = max(maxVal, node.val)
            left = dfs(node.left, maxVal)
            right = dfs(node.right, maxVal)
        dfs(root, root.val)
        return res