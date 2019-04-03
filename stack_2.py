from linked_list import LinkedList


class Stack:
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """ Pushes a new element to the top of the stack"""
        self.ll.insert_first(new_element)

    def pop(self):
        """ Pops the first element from the top of a stack and returns it """
        return self.ll.delete_first()
