class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class SList:
  def __init__(self):
    self.head = None
  
  def append(self, val):
    # make a new node, with value set to val
    node = Node(val)
    # if there are no nodes, set self.head to new node
      # how do we tell that there are no nodes?
    if self.head == None:
      self.head = node
    # make last node's .next point to the new node
    else:
      curr = self.head
      while(curr.next != None):
        curr = curr.next
      curr.next = node
    return self

  def display(self):
    if self.head == None:
      print(None)
    else:
      curr = self.head
      result = []
      while(curr):
        result.append(curr.value)
        curr = curr.next
      print(result)
    return self

# SList {
#   head: {
#     val: A,
#     next: {
#       val: B,
#       next: {
#         val: C,
#         next: {
#           val: D,
#           next: None
#         }
#       }
#     }
#   }
# }

slist = SList()
slist.append('A').display().append('B').display().append('C').display()