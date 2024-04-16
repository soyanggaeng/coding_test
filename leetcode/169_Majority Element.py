# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        answer = 0
        count_num = 0
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for n in nums:
            if answer == n:
                continue
            if count[n] > count_num:
                count_num = count[n]
                answer = n
        return answer
