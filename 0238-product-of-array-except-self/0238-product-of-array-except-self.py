class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = 1
        count0 = 0
        index = -1
        for i, n in enumerate(nums):
            if n != 0:
                result *= n
            else:
                count0 += 1
                index = i
        
        
        if count0 == 0:
            answer = []
            for i in range(len(nums)):
                answer.append(result / nums[i])
            return answer
        
        elif count0 == 1:
            answer = [0] * len(nums)
            answer[index] = result
            return answer
                
        return [0] * len(nums)
