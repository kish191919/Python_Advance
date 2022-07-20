class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        print(self.val)
        print(self.left)
        print(self.right)


# class Solution:
#     def sortedArrayToBST(self, nums):
#         if nums:
#             mid = len(nums) // 2
#             # print(mid)
#             root = TreeNode(nums[mid])
#             root.left = self.sortedArrayToBST(nums[:mid])
#             # print(root.left)
#             root.right = self.sortedArrayToBST(nums[mid+1:])
#             # print(root.right)
#             return root


class Solution:
    def sortedArrayToBST(self, nums):
        if nums:
            mid = len(nums)//2

            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])

            return root

