class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if c == ')':
                    expected = '('
                elif c == '}':
                    expected = '{'
                else:
                    expected = '['
                if not stack or stack.pop() != expected:
                    return False
        if stack:
            return False
        return True
        