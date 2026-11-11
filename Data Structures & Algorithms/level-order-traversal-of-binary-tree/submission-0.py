# Definition for a binary tree node.
# class TreeNode:
#     def __init__(Deque, self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rootLevels = []
        if not root:
          return rootLevels

        queue = deque()

        queue.append(root)
       
        level = 0
        
        while len(queue) > 0:

          for i in range(len(queue)):
            node = queue.popleft()

            if level == len(rootLevels):
              rootLevels.append([])

            rootLevels[level].append(node.val)

            if node.left:
              queue.append(node.left)
            
            if node.right:
              queue.append(node.right)
          # print(level, rootLevels[level])
          level += 1

        return rootLevels
