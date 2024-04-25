# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        
        answer = ""
        leftover = 0
        for i in range(len(a)-1, -1, -1):
            if int(a[i]) + int(b[i]) + leftover > 1:
                now = int(a[i]) + int(b[i]) + leftover - 2 
                leftover = 1
            else:
                now = int(a[i]) + int(b[i]) + leftover
                leftover = 0
            answer = str(now) + answer
        if leftover == 1:
            answer = "1" + answer
            
        return answer
            
