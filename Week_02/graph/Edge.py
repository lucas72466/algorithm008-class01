"""
表达有权图中的边
"""


class Edge(object):

    def __init__(self, vertex_a, vertex_b, weight):
        self.a = vertex_a
        self.b = vertex_b
        self.weight = weight

    @property
    def vertex_a(self):
        return self.a

    @property
    def vertex_b(self):
        return self.b

    @property
    def weight_(self):
        return self.weight

    def other(self, vertex):
        assert vertex == self.a or vertex == self.b
        return self.a if vertex == self.b else self.b

    def __str__(self):
        string = '{}--{}: {}'.format(self.a, self.b, self.weight)
        return string

    def __lt__(self, other):
        return self.weight < other.weight_

    def __gt__(self, other):
        return self.weight > other.weight_

    def __le__(self, other):
        return self.weight <= other.weight_

    def __ge__(self, other):
        return self.weight >= other.weight_

    def __eq__(self, other):
        return self.weight == other.weight_



