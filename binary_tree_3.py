class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


if __name__ == "__main__":
    r = BinaryTree('a')
    r.insertLeft('b')
    r.leftChild.insertRight('d')
    r.insertRight('c')
    r.rightChild.insertLeft('e')
    r.rightChild.insertRight('f')

    print(r.getRightChild().getRootVal())
    print(r.getLeftChild().getRightChild().getRootVal())
    print(r.getRightChild().getLeftChild().getRootVal())
