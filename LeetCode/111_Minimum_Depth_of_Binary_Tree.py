import collections

# deque

# class Solution:
#     def minDepth(self, root):
#         if not root:
#             return 0
#
#         q = collections.deque()
#         q.append((root, 1))
#
#         while q:
#             node, depth = q.popleft()
#             if not node.left and not node.right:
#                 return depth
#
#             if node.left:
#                 q.append((node.left, depth + 1))
#             if node.right:
#                 q.append((node.right, depth + 1))


class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.right and root.left:
            return 1 + self.minDepth(root.left)

        if not root.left and root.right:
            return 1 + self.minDepth(root.right)

        return 1 + min(self.minDepth(root.left),self.minDepth(root.right) )


