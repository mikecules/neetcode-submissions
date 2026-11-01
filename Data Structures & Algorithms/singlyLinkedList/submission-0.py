class Node:
  def __init__(self, val: int | None = None):
    self.next: Node | None = None
    self.value: int | None = val

class LinkedList:
    
    def __init__(self):
        self.root: Node | None = None
        self.length: int = 0

    
    def get(self, index: int) -> int:
      node: Node | None = self.root
      j = 0

      while node:
        if j == index:
          return node.value

        node = node.next
        j+= 1

      return -1
        

        

    def insertHead(self, val: int) -> None:
      self.length += 1
      n = Node(val)
      
      if self.root:
        n.next = self.root

      self.root = n

    def insertTail(self, val: int) -> None:
      self.length += 1
      node = self.root
      n = Node(val)

      if not node:
        self.root = n
        return

      while node.next:
        node = node.next

      node.next = n

        

    def remove(self, index: int) -> bool:
      if not self.root:
        return False
      
      node = self.root
      prev_node: Node | None = None
      j = 0

      while node:
        if j == index:
          if prev_node:
            prev_node.next = node.next
            node.next = None
          else:
            new_root = self.root.next
            self.root.next = None
            self.root = new_root

          self.length = max(0, self.length - 1)
          return True
        j += 1

        prev_node = node
        node = node.next

      return False

    def getValues(self) -> List[int]:
      vals: List[int] = []

      node: Node | None = self.root

      while node:
        vals.append(node.value)
        node = node.next

      return vals

        
