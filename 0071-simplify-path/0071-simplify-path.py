class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        result = []

        for s in paths:
            if s == "." or not s:
                continue
            elif s == "..":
                if result:
                    result.pop()
            else:
                result.append(s)
        
        return "/" + "/".join(result)
    

        