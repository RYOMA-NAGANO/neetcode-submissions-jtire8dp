# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, stack, maxVal):
        if not root:
            return
        if root.val >= maxVal:
            stack.append(root.val)
        maxVal = max(maxVal, root.val)
        self.dfs(root.left, stack, maxVal)
        self.dfs(root.right, stack, maxVal)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        self.dfs(root, res, root.val)
        return len(res)
