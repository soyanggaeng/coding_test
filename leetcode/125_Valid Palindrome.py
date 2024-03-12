# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # 왼쪽 포인터가 알파벳 혹은 숫자가 아닐 때 건너뛰기
            while left < right and not ('A' <= s[left] <= 'Z' or 'a' <= s[left] <= 'z' or '0' <= s[left] <= '9'):
                left += 1
            # 오른쪽 포인터가 알파벳 혹은 숫자가 아닐 때 건너뛰기
            while left < right and not ('A' <= s[right] <= 'Z' or 'a' <= s[right] <= 'z' or '0' <= s[right] <= '9'):
                right -= 1     

            # 소문자로 변환 (대문자일 경우 32를 더함)
            if 'A' <= s[left] <= 'Z':
                left_word = chr(ord(s[left]) + 32)
            else:
                left_word = s[left]

            if 'A' <= s[right] <= 'Z':
                right_word = chr(ord(s[right]) + 32)
            else:
                right_word = s[right]
            
            # 비교
            if left_word != right_word:
                return False

            left += 1
            right -= 1

        return True
