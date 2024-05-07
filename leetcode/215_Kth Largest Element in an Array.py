# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # A min-heap ensures that the smallest element is always at the top (index 0).
        # When you pop elements from the heap, you are essentially removing the smallest elements.
        # If you remove n-k smallest elements, the top of the heap becomes the kth largest element. This is because after removing n-k elements, k elements remain and the smallest among those k elements is the kth largest in the entire list.

        # Convert the input list to a min-heap
        heap = nums[:]
        heapq.heapify(heap)
        # print(heap) # 1, 2, 3, 5, 6, 4
        
        # Pop elements from the heap until the kth largest is found
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        
        # print(heap) # 5, 6
        
        return heap[0]
