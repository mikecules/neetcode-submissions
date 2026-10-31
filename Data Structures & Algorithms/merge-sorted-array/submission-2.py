class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0


        if n == 0:
            return
        elif m == 0:
            while j < n:
                nums1[j] = nums2[j]
                j += 1

            return

        cheat_arr = []

        while i < m and j < n:
            a = nums1[i]
            b = nums2[j]

            if a >= b:
                cheat_arr.append(b)
                j += 1
            else:
                i += 1
                cheat_arr.append(a)
        

        while i < m:
            cheat_arr.append(nums1[i])
            i += 1

        while j < n:
            cheat_arr.append(nums2[j])
            j += 1

        i = 0

        for n in cheat_arr:
            nums1[i] = n
            i += 1

