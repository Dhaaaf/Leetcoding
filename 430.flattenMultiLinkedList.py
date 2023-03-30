# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Solution 1
        if not head:
            return None
        
        dummy = Node(-1)
        dummy.next = head
        prev = dummy
        stack = [head]
        
        while stack:
            curr = stack.pop()
            
            prev.next = curr
            curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            prev = curr
        
        dummy.next.prev = None
        return dummy.next
    

    # SOlution 2 easier to read?
    #     current = head
    #     stack = []

    #     while current:
    #         if current.child:
    #             if current.next:
    #                 stack.append(current.next)
    #             current.next = current.child
    #             current.next.prev = current
    #             current.child = None

    #         if not current.next and stack:
    #             current.next = stack.pop()
    #             current.next.prev = current

    #         current = current.next

    #     return head
