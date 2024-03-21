# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10
 

# Constraints:

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
 

# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottom up
        dp = triangle[-1]

        # start from the second to last row and move upwards
        for i in range(len(triangle) - 2, -1, -1):
            # 각 행에 대해 해당 행의 모든 요소 순회 
            for j in range(len(triangle[i])):
                # triangle[i][j]: 현재 요소
                # dp[j], dp[j+1]: 그 요소에서 내려갈 수 있는 두 경로 중 더 작은 경로 합 
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

        return dp[0]
