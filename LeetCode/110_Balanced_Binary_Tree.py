# class Solution:
#     def isBanaced(self, root):
#         def check(root):
#             if root is None:
#                 return 0
#             left = check(root.left)
#             right = check(root.right)
#             if left == -1 or right == -1 or abs(left - right)>1:
#                 return -1
#             return 1+max(left, right)
#
#         return check(root) !=-1


class Solution:
    def isBalanced(self, root):

        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1])  <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


