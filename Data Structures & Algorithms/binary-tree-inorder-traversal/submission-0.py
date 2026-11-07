# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversalHelper(self, root: TreeNode | None, traverseList: List[int]) -> List[int]:
      if not root:
        return []

      current = root
      
      if current.left:
        self.inorderTraversalHelper(current.left, traverseList)
        
      traverseList.append(current.val)

      if current.right:
        self.inorderTraversalHelper(current.right, traverseList)

      return traverseList

      
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
          return []

        current = root

        print(current)
        
        # while current:
        #   if current.left:

        return self.inorderTraversalHelper(root, [])


