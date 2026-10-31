class MinStack:
  def __init__(self):
    self.stack = []
    self.stack_snapshot_by_len = dict()

  def push(self, val: int) -> None:
    self.stack.append(val)
    l = len(self.stack)

    prev_min = self.stack_snapshot_by_len.get(str(l - 1), None)
    k = str(l)

    if prev_min is None:
      self.stack_snapshot_by_len[k] = val
    else:
      self.stack_snapshot_by_len[k] = min(prev_min, val)

  def pop(self) -> None:
    l = len(self.stack)
    if l == 0:
      return

    del self.stack_snapshot_by_len[str(l)]
    self.stack.pop()

  def top(self) -> int:
    return self.stack[len(self.stack) - 1]

  def getMin(self) -> int:
    return self.stack_snapshot_by_len.get(str(len(self.stack)), None)
