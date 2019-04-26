class minHeap:

    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.percUp(self.size)

    def percDown(self, i):
        while (i * 2) <= self.size:
            min = self.minChild(i)
            if self.heapList[i] > min:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[min]
                self.heapList[min] = temp
            i = min

    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval


    # def heapSort(self):


            # def buildHeap(self, alist):
    #     i = len(alist // 2)
    #     self.size = len(alist)
    #     self.heapList = [0] + alist[:]
    #     while i > 0:
    #         self.percDown(i)
    #         i -= 1

class heap:

    def __init__(self):
        self.heapList = [0]
        self.size = 0
        self.arr = []

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.percUp(self.size)

    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        while (i * 2) <= self.size:
            min = self.minChild(i)
            if self.heapList[i] > self.heapList[min]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[min]
                self.heapList[min] = tmp
            i = min

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def heapSort(self):
        while self.size > 0:
            tmp = self.heapList[1]
            self.heapList[1] = self.heapList[self.size]
            self.heapList[self.size] = tmp
            val = self.heapList.pop()
            self.size -= 1
            self.arr.append(val)
            self.percDown(1)


heap = heap()
heap.insert(4)
heap.insert(9)
heap.insert(10)
heap.insert(11)
heap.delMin()
heap.insert(5)
heap.insert(123)
heap.insert(32)
heap.insert(12)
heap.insert(17)
heap.insert(19)
print(heap.heapList)
heap.heapSort()
print(heap.heapList)
print(heap.arr)

# newheap = minHeap()
# newheap.buildHeap([1, 5, 34,2, 5, 7,3 ,57,6 ,7 ])
# print(newheap.heapList)