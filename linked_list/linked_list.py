from node import Node

class LinkedList(object):
    """docstring for ."""
    def __init__(self):
        self.head = None


    def set_head(self, head_node):
        self.head = head_node

    """ push an element on front of the list"""
    def push(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.set_head(node)

    """ append an element at the end of the list"""
    def append(self, value):
        node = Node(value)
        current = self.head
        if not current:
            self.head = node
            return

        while current.get_next():
            current = current.get_next()

        current.set_next(node)

    """ pop an element from the front of the list"""
    def pop(self):
        if self.head:
            self.head = self.head.get_next()
        else:
            raise IndexError("Unable to pop, empty list")

    """ delete all value from the list"""
    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                    current = current.get_next()
                else:
                    self.head = current.get_next()
                    current = self.head
            else:
                prev = current
                current = current.get_next()


    """ return True id the list contains the element """
    def contains(self, value):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()

        return found


    """ print the length of the list """
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count


    def __str__(self):
        current = self.head
        output = ""
        while current:
            if current.get_next():
                output += str(current) + " -> "
            else:
                output += str(current)
            current = current.get_next()
        return output
