class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        chunk = []
        size = 0
        temp = []
        for i, word in enumerate(words):
            if size + len(temp) + len(word) <= maxWidth:
                temp.append(word)
                size += len(word)
            else:
                chunk.append(temp.copy())
                temp = [word]
                size = len(word)

        if temp:
            chunk.append(temp)
        
        result = []
        for i, line in enumerate(chunk):
            if i == len(chunk)-1:
                result.append(" ".join(line).ljust(maxWidth, " "))
            
            elif len(line) == 1:
                result.append(line[0].ljust(maxWidth, " "))
            
            else:
                l = sum([len(x) for x in line])
                d, m = divmod(maxWidth-l, len(line)-1)
                temp = line[0]
                for w in line[1:]:
                    blank = d+1 if m > 0 else d
                    temp += " " * blank
                    temp += w
                    m -= 1
                result.append(temp)
            
        return result
                    



        
        return result