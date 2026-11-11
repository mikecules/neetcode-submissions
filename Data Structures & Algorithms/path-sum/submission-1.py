# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _hasPathSumHelper(self, root: TreeNode, targetSum: int, currentSum: int = 0) -> bool:
   
      currentSum += root.val

      if not root.left and not root.right:
        return targetSum == currentSum

      if root.left and self._hasPathSumHelper(root.left, targetSum, currentSum):
        return True
      
      if root.right and self._hasPathSumHelper(root.right, targetSum, currentSum):
        return True

      #currentSum -= root.val

      return False


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
      if not root:
        return False

      return self._hasPathSumHelper(root, targetSum)

      
        