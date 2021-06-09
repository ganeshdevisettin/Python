class Stack:
  def __init__(self):
    self.stack = []
        
  def push(self, ch):
    self.stack.append(ch)
    
  def pop(self):
    toReturn = self.stack[-1]
    self.stack = self.stack[:-1]
    return toReturn
  
  def peek(self):
    return self.stack[-1]
  
  def print(self):
    for x in range(len(self.stack)-1):
      print(self.stack[x], end=', ')
    print(self.stack[-1])
