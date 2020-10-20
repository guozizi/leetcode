# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        DFS 深度优先 后序遍历
        """
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        """
        BFS 广度优先
        """
        if not root:return 0
        queue, count = [root] , 0
        while queue:
            tmp = []
            for item in queue:
                if item.left:
                    tmp.append(item.left)
                if item.right:
                    tmp.append(item.right)
            queue = tmp
            count += 1
        return count