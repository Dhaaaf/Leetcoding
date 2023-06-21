print("Hello")

# iterate through the array:
# for each element check if its an array
# If it's an array we call the function again
# if it's a zero, then we delete the element.
# return array

# Coorect doe
def remove_zeros(lst):
  list1 = []
  
  for i in lst:
    if type(i) is list:
      list1.append(remove_zeros(i))  # Handle nested lists with recursive call
    elif type(i) is int and i != 0:  # Check if type is int and not 0
      list1.append(i)
      
  return list1
      
print(remove_zeros([0, 0, 5, [0, 0], [0, 16]]))
      






# // Your last Python3 code is saved below:
# // # Creat a node class.
# // # >>> # Node needs to have, val, string, next
# // # >>> # Create the list

# // class ListNode:
# //   def __init__(self, val = 0, string = "", next = None):
# //     self.val = val
# //     self.string = string
# //     self.next = next

# // def create_list():
# //   node7 = ListNode(13, "Green", None)
# //   node6 = ListNode(8, "Red", node7)
# //   node5 = ListNode(8, "Green", node6)
# //   node4 = ListNode(5, "Red", node5)
# //   node3 = ListNode(3, "Red", node4)
# //   node2 = ListNode(2, "Green", node3)
# //   node1 = ListNode(2, "Green", node2)
  
# //   curr = node1
# //   while curr:
# //     print(curr.val, curr.string)
# //     curr = curr.next
    
# // create_list()
    

# // # Each node:
# // # 2, Green
# // # 2, Green
# // # 3, Red
# // # 5, Red
# // # 8, Green
# // # 8, Red
# // # 13, Green