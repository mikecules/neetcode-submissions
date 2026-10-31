# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        pairs_len = len(pairs)
        
        iteration_sort_history: List[List[Pair]] = []

        if pairs_len == 0:
            return iteration_sort_history
        elif pairs_len == 1:
             iteration_sort_history.append(pairs)
             return iteration_sort_history

        new_pairs_list = pairs.copy()

        for i in range(pairs_len):
            new_pairs_list = new_pairs_list.copy()

            if i == 0:
                iteration_sort_history.append(new_pairs_list)
                continue
            
            j = i
            
            while j >= 1 and new_pairs_list[j - 1].key > new_pairs_list[j].key:
                new_pairs_list[j - 1], new_pairs_list[j] = new_pairs_list[j],  new_pairs_list[j - 1]
                j -= 1
            
            iteration_sort_history.append(new_pairs_list)

        return iteration_sort_history