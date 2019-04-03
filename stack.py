class Stack:

    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


# O(N) time, O(N) space
def revstring(str):
    st = Stack()
    for c in str:
        st.push(c)

    revstr = ''
    while not st.isEmpty():
        revstr = revstr + st.pop()

    return revstr


def parChecker(symbolStr):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolStr) and balanced:
        c = symbolStr[index]

        if c in "([{":
            s.push(c)
        elif s.isEmpty():
            balanced = False
        else:
            top = s.pop()
            if not matches(top, c):
                balanced = False

        index += 1

    if s.isEmpty() and balanced:
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


if __name__ == "__main__":
    s = Stack()

    print(s.isEmpty())
    print(s.push(4))
    print(s.push('dog'))
    print(s.peek())
    print(s.push(True))
    print(s.size())
    print(s.isEmpty())
    print(s.push(8.4))
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.items)

    string = 'hallehula'
    print(revstring(string))

    print(parChecker('((()))'))
    print(parChecker('(()'))
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))

    print(baseConverter(25, 2))
    print(baseConverter(25, 16))
    print(baseConverter(25, 8))
    print(baseConverter(256, 16))
