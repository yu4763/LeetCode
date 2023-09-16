class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answers = []
        while temperatures:
            cur = temperatures.pop()
            cnt = 0
            while stack and stack[-1][0] <= cur:
                cnt += stack.pop()[1]
            if stack:
                answers.append(cnt + 1)
                stack.append((cur, cnt + 1))
            else:
                answers.append(0)
                stack.append((cur, 1))

        answers.reverse()
        return answers
        