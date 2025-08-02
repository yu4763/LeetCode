class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, n in enumerate(nums):
            maps[n] = i
        
        for i, n in enumerate(nums):
            need = target - n
            if need in maps and maps[need] > i:
                return [i, maps[need]]
        