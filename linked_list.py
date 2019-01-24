class Element:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """ Appends a new element to the end of the list """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """ Gets the element at the index of position """
        if self.head:
            current = self.head
            for i in range(position - 1):
                current = current.next
            return current
        else:
            return None

    def insert(self, new_element, position):
        """ Inserts a new element at position """
        if self.head:
            current = self.head
            for i in range(position - 2):
                current = current.next
            new_element.next = current.next
            current.next = new_element

    def delete(self, value):
        """ Deletes the first element with the value passed """
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_first(self, new_element):
        """ Inserts a new element at the start of the list """
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """ Deletes the element at the start of the list"""
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted
