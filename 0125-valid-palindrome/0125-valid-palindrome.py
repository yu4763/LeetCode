class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        fixed = [c.lower() for c in s if c.isalpha() or c.isnumeric()]
        return fixed == list(reversed(fixed))


        