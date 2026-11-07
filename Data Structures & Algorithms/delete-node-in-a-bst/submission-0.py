# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self,  root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        current: TreeNode = root

        while current.left:
            current = current.left

        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # key == root.val
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode: TreeNode | None = self.findMinNode(root.right)
                if minNode:
                    root.val = minNode.val
                    root.right = self.deleteNode(root.right, minNode.val)
            
        return root
            
            
