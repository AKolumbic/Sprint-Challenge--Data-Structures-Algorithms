class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # recursive
    # call the cb on the current BST node
    # cb(self.value)
    # if self.left:
    #   self.left.depth_first_for_each(cb)
    # if self.right:
    #   self.right.depth_first_for_each(cb)
    # return

    # Iterative
    stack = []
    # we're at the top-most node(root node)
    # append root node
    stack.append(self)
    # iterate through elements in stack
    while len(stack):
      # pop off top-most stack element
      current_node = stack.pop()
      # check if node has right child
      if current_node.right:
        stack.append(current_node.right)
      # check if node has a left child
      if current_node.left:
        stack.append(current_node.left)
      # call the callback
      cb(current_node.value)


  def breadth_first_for_each(self, cb):
    # my attempt, does not work
    # cb(self.value)
    # this_lvl = [self.left, self.right]
    # while this_lvl:
    #   nxt_lvl = []
    #   for n in this_lvl:
    #     if n.left:
    #       nxt_lvl.append(n.left)
    #     if n.right:
    #       nxt_lvl.append(n.right)
    #   this_lvl = nxt_lvl

    q = []
    q.append(self)
    while len(q):
      current_node = q.pop(0)
      if current_node.left:
        q.append(current_node.left)
      if current_node.right:
        q.append(current_node.right)
      cb(current_node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
