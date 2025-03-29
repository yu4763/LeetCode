class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        answer = 0
        max_height = max(height)
        max_place = height.index(max_height)
        
        left_max = height[0]
        right_max = height[-1]
        
        for i in range(max_place):
            left_max = max(left_max, height[i])
            answer += left_max - height[i]
        
        for i in range(len(height)-1, max_place, -1):
            right_max = max(right_max, height[i])      
            answer += right_max - height[i]      
        
        return answer                    