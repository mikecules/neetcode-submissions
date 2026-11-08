class DynamicArray:
    
    def __init__(self, capacity: int):
      self.length_elements_array = 0
      self.capacity_array = capacity
      self.array: List[int | None] = [None] * capacity 



    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
      if self.array[i] == None:
          self.length_elements_array += 1

      self.array[i] = n


    def pushback(self, n: int) -> None:
      if self.length_elements_array >= self.capacity_array:
        self.resize()

      self.array[self.length_elements_array] = n
      self.length_elements_array += 1
      


    def popback(self) -> int:
      print(self.length_elements_array, self.array)
      if self.length_elements_array > 0:
        nextIndex = self.length_elements_array - 1
        n = self.array[nextIndex]
        self.length_elements_array = nextIndex
        return n

    def resize(self) -> None:
      newArray = [None] * self.capacity_array
      self.array = self.array + newArray
      self.capacity_array *= 2


    def getSize(self) -> int:
      return self.length_elements_array 
        
    
    def getCapacity(self) -> int:
      return self.capacity_array 
