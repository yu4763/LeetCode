class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                top = stack.pop()
                answer[top[1]] = i - top[1]
            else:
                stack.append((temperatures[i], i))
        return answer
