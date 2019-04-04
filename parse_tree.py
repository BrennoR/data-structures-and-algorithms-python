from binary_tree_3 import BinaryTree
from stack import Stack
import operator


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i in ['+', '-', '/', '*']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            try:
                currentTree.setRootVal(i)
                currentTree = pStack.pop()

            except:
                raise ValueError("Token {} is not a valid integer.".format(i))

    return eTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return int(parseTree.getRootVal())


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt_2 = buildParseTree("( 3 + ( 4 * 5 ) )")
print(evaluate(pt))
print(evaluate(pt_2))
