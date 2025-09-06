class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        num_sets = set(nums)
        results = []
        for n in num_sets:
            if n-1 not in num_sets:
                start = n
                current = start + 1
                while current in num_sets:
                    current += 1
                if current -1 == start:
                    results.append(f"{start}")
                else:
                    results.append(f"{start}->{current-1}")
        return sorted(results, key=lambda x: int(x.split("->")[0]))
                



        