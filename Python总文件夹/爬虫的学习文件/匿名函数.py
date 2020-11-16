# Definition for a binary tree node.
from collections import Counter
import fasttext
import nltk
nltk.download('stopwords')

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
#
#
# class Solution:
#     def postorderTraversal(self, root: TreeNode):
#         res = []
#         if not root:
#             return res
#         stack = [root]
#         while len(stack) > 0:
#             top = stack.pop()
#             res.append(top.val)
#             if top.left:
#                 stack.append(top.left)
#             if top.right:
#                 stack.append(top.right)
#         res.reverse()
#         return res
# x = Solution()
# print(x.postorderTraversal([1,2,3]))
# model = fasttext.train_supervised()