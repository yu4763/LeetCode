class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            print(p1, p2, nums1)
            if (nums1[p1] < nums2[p2]):
                p1 += 1
            else:
                nums1.pop()
                nums1.insert(p1, nums2[p2])
                p1 += 1
                p2 += 1
        
        print(nums1, p1, p2)
        for p in range(p2, n):
            nums1.pop()
        print(nums1)
        for p in range(p2, n):
            target = len(nums1) -1
            while target > 0 and nums1[target] > nums2[p]:
                target -= 1
            nums1.insert(target+1, nums2[p])

        
        
        

        