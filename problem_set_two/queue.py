class Queue:
  def __init__(self):
    self.root_node = None

  def add(self, data):
    new_node = Node(data)

    if self.root_node is None:
      self.root_node = new_node
      return

    current_node = self.root_node
    next_node = self.root_node.get_next_node()
    while next_node is not None:
      current_node = next_node
      next_node = next_node.get_next_node()

    next_node = new_node
    current_node.set_next_node(next_node)

  def remove(self):
    if self.root_node is None:
      return

    current_node = self.root_node
    prev_node = None
    next_node = self.root_node.get_next_node()

    if next_node is None:
      data = self.root_node.get_data()
      self.root_node = None
      return data
    else:
      while next_node is not None:
        prev_node = current_node
        current_node = next_node
        next_node = next_node.get_next_node()

      data = current_node.get_data()
      prev_node.set_next_node(None)
      return data

  def peek(self):
    if self.root_node is None:
      return None

    current_node = self.root_node
    next_node = self.root_node.get_next_node()

    if next_node is None:
      return self.root_node.get_data()
    else:
      while next_node is not None:
        current_node = next_node
        next_node = next_node.get_next_node()
      return current_node.get_data()

  def size(self):
    if self.root_node is None:
      return 0

    count = 1
    next_node = self.root_node.get_next_node()
    while(next_node is not None):
      count = count + 1
      next_node = next_node.get_next_node()

    return count

  def isEmpty(self):
    return self.root_node is None


class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = None

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

  def get_data(self):
    return self.data


def test_queue():
  queue = Queue()
  print('Test: is Stack Empty?', queue.isEmpty() == True)
  queue.add(1)
  print('Test: Stack Size', queue.size() == 1)
  queue.add(2)
  print('Test: Stack Size', queue.size() == 2)

  removed_item = queue.remove()
  print('Test: Stack Size after removing item', queue.size() == 1)
  print('Test: pop', removed_item == 2)

  queue.add(3)
  peeked_item = queue.peek()
  print('Test: Stack Size after pop', queue.size() == 2)
  print('Test: pop', peeked_item == 3)
  print('Test: is Stack Empty?', queue.isEmpty() == False )


test_queue()
