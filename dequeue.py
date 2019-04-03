class Dequeue:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def pal_checker(aString):
    char_dequeue = Dequeue()

    for c in aString:
        char_dequeue.add_rear(c)

    stillEqual = True

    while char_dequeue.size() > 1 and stillEqual:
        first = char_dequeue.remove_front()
        last = char_dequeue.remove_rear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == "__main__":
    print(pal_checker("lsdkjfskf"))
    print(pal_checker("radar"))
