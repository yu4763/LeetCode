class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left+1, right+1]
            
            elif current < target:
                left += 1
            
            else:
                right -= 1

        