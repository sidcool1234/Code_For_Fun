class Stack:
  def __init__(self):
    self.node = None

  def push(self, data):
    if self.node is None:
      self.node = Node(data)
      return

    new_node = Node(data)
    new_node.set_next_node(self.node)
    self.node = new_node

  def pop(self):
    if self.node is None:
      return None

    next_node = self.node.get_next_node()
    root_node = self.node
    self.node = next_node
    return root_node.get_data()

  def peek(self):
    if self.node is None:
      return None
    return self.node.get_data()

  def isEmpty(self):
    return self.node is None

  def size(self):
    if self.node is None:
      return 0

    count = 1
    next_node = self.node.get_next_node()
    while(next_node is not None):
      count = count + 1
      next_node = next_node.get_next_node()

    return count


class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None

  def set_next_node(self, next_node):
    self.next_node = next_node

  def is_data_present(self):
    return self.data is None

  def get_next_node(self):
    return self.next_node

  def get_data(self):
    return self.data

def test_stack():
  stack = Stack()
  print('Test: is Stack Empty?', stack.isEmpty() == True)
  stack.push(1)
  print('Test: Stack Size', stack.size() == 1)
  stack.push(2)
  print('Test: Stack Size', stack.size() == 2)
  popped_item = stack.pop()
  print('Test: Stack Size after pop', stack.size() == 1)
  print('Test: pop', popped_item == 2)

  stack.push(3)
  peeked_item = stack.peek()
  print('Test: Stack Size after pop', stack.size() == 2)
  print('Test: pop', peeked_item == 3)

  print('Test: is Stack Empty?', stack.isEmpty() == False )

test_stack()