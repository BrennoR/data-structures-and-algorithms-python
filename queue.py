class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def hot_potato(name_list, num):
    simQueue = Queue()
    for name in name_list:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())

        simQueue.dequeue()

    return simQueue.dequeue()


if __name__ == "__main__":
    q = Queue()

    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.items)

    print(q.size())
    print(q.isEmpty())
    print(q.enqueue(8.4))
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.items)

    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

