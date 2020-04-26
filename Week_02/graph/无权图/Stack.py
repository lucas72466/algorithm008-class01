

class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, element):
        return self.data.append(element)

    def pop(self):
        ret = self.data.pop()
        return ret

    def peek(self):
        return self.data[0]

    def size(self):
        return len(self.data)

    def show(self):
        for i in self.data:
            print(i, end=' ')


