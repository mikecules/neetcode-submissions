class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_len = len(matrix)

        if matrix_len == 0:
          return False

        top = 0
        bottom = matrix_len - 1
        left = 0
        right = len(matrix[0]) - 1
        right_most_idx = right
        mid_row = 0
        mid = 0
        n = 0

        # find row


        while top <= bottom and left <= right:
          mid_row = (top + bottom) // 2
          if top != bottom:
            n = matrix[mid_row][right]
            if n == target:
              return True
            elif n > target and target >= matrix[mid_row][0]:
              top = mid_row
              bottom = top
            elif n > target:
              bottom = mid_row - 1
            else:
              top = mid_row + 1
          else:
            mid = (left + right) // 2
            n = matrix[top][mid]
            if matrix[top][mid] == target:
              return True
            elif n > target:
              right = mid - 1
            else:
              left = mid + 1

        return False