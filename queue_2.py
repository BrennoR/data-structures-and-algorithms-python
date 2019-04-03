class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        """ Adds a new element to the queue """
        self.storage.append(new_element)

    def peek(self):
        """ Returns the first element in the queue """
        return self.storage[0]

    def dequeue(self):
        """ Delete and return the first element in the queue """
        return self.storage.pop(0)
