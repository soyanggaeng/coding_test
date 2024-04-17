# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top, bottom, left, right = 0, m-1, 0, n-1
        result = []

        while top <= bottom and left <= right:
            # traverse from left to right along the top row
            ## 1, 2, 3
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1 

            # traverse from top to bottom along the right column
            ## 3, 6, 9
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # traverse from right to left along the bottom row
                ## 9, 8, 7
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                # traverse from bottom to top along the left column
                ## 7, 4
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
            
        return result
