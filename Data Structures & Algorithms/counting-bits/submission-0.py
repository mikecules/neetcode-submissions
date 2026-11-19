class Solution:
    def countBits(self, n: int) -> List[int]:
        listBits = []
        sumBits = 1

        def countBits(j: int):
            total = 0

            while j > 0:
                if j & 1:
                    total += 1

                j = j >> 1

            return total


        for i in range(n + 1):
            listBits.append(countBits(i))

        return listBits