class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        from collections import Counter
        counts = Counter(nums)
        target_counts = counts[val]
        for i in range(target_counts):
            nums.remove(val)
        return len(nums)
        