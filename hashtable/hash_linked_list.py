class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

    def delete(self, value):
        curr = self.head
        if curr.value == value:
            self.head = curr.next
            return curr
        
        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:

                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
        return None


    
    def find(self, value):
        curr = self.head

        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None