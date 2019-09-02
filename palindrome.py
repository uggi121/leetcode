class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        substring = "".join(char.lower() for char in s if char.isalnum())
        return substring == substring[::-1]