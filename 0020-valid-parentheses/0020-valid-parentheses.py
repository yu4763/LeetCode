class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if l in {"(", "{", "["}:
                stack.append(l)
            
            elif not stack:
                return False

            elif l == ")" and stack.pop() != "(":
                return False
            
            elif l == "}" and stack.pop() != "{":
                return False
            
            elif l == "]" and stack.pop() != "[":
                return False
        
        if stack:
            return False
        
        return True