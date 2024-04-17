# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_in_window = set()
        max_len = 0
        left = 0

        for right in range(len(s)):
            # print("s[right]:", right, s[right])
            while s[right] in chars_in_window:
                # remove the character at the left index to ensure no duplicates are in the window
                # print("s[left]:", left, s[left])
                chars_in_window.remove(s[left])
                left += 1
            # add the current character and update the maximum length
            chars_in_window.add(s[right])
            max_len = max(max_len, right - left + 1)
            # print("chars_in_window, left, max_len", chars_in_window, left, max_len)

        return max_len
