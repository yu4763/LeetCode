class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        splits = s.split()
        return " ".join(reversed(splits))
        