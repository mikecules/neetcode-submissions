# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      rightBranchNodes: List[int] = []
      nodesPerLevel: List[List[int]] = []

      if not root:
        return rightBranchNodes

      queue = deque()
      queue.append(root)
      level = 0

      while len(queue) > 0:
        for i in range(len(queue)):
          current = queue.popleft()

          if level == len(nodesPerLevel):
            nodesPerLevel.append([])

          nodesPerLevel[level].append(current.val)

          if current.right:
            queue.append(current.right)

          if current.left:
            queue.append(current.left)
          
        level += 1

      for nodesAtLevel in nodesPerLevel:
        rightBranchNodes.append(nodesAtLevel[0])

      return rightBranchNodes
        