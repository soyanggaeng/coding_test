# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        # base case
        if len(s) == 0 or len(s) == 1:
            return False

        stack = []

        for string in s:
            if string == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(':
                    stack = stack[:-1]
                else:
                    return False
            elif string == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '{':
                    stack = stack[:-1]
                else:
                    return False                
            elif string == ']': 
                if len(stack) == 0:
                    return False
                elif stack[-1] == '[':
                    stack = stack[:-1]
                else:
                    return False      
            else:
                stack.append(string)

        if len(stack) == 0:
            return True
        else:
            return False
