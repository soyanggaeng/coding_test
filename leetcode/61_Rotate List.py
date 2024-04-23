# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case 
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        current.next = head

        # find the number of effective rotations
        k = k % length
        if k == 0:
            current.next = None
            return head

        steps_to_new_tail = length - k
        new_tail = head
        # print(new_tail.val)
        for i in range(steps_to_new_tail - 1):
            new_tail =new_tail.next
        # print(new_tail.val)        

        new_head = new_tail.next
        # print(new_head.val)

        new_tail.next = None

        return new_head
