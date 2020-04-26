

class Queue(object):

    def __init__(self):
        self.data = []

    def en_queue(self, element):
        self.data.append(element)

    def de_queue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)