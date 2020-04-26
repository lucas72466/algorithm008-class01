"""
稀疏图--邻接表 不考虑平行边， 允许自环边
"""
import numpy as np


class SparseGraph:

    def __init__(self, vertex, directed):
        self.v = vertex  # 节点的数量 vertex
        self.e = 0  # 边的数量 edge 初始时默认没有边
        self.directed = directed  # 是否为有向图
        self.info = {v: [] for v in range(vertex)}

    @property
    def num_of_vertex(self):
        return self.v

    @property
    def edge(self):
        return self.e

    def add_edge(self, n, m):
        assert self.v > n >= 0, '请输入正确的节点'
        assert self.v > m >= 0, '请输入正确的节点'

        self.info[n].append(m)
        if n != m and not self.directed:
            self.info[m].append(n)

        self.e += 1

    def has_edge(self, n, m):
        assert self.v > n >= 0, '请输入正确的节点'
        assert self.v > m >= 0, '请输入正确的节点'

        for i in range(len(self.info[n])):
            if self.info[n][i] == m:
                return True
            return False

    def show(self):
        for i in range(self.v):
            print(i, end=': ')
            for vertex in self.info[i]:
                print(vertex, end=' ')
            print()

    def get_edge_iterator(self, vertex):
        out_class = self

        class EdgeIterator:
            """
            临边迭代器 用来向外部提供查寻临边状态的接口，并且和稀疏图实现统一，方便算法实现
            """

            def __init__(self, v):
                self.graph = out_class  # 图的引用
                self.v = v
                self.index = 0  # 将初始索引设为-1

            def begin(self):
                """
                返回图中与顶点vertex相连接的第一个顶点
                """
                self.index = 0
                if len(self.graph.info[self.v]):
                    return self.graph.info[self.v][self.index]
                return -1

            def next(self):
                """
                返回图中与顶点vertex相连接的下一个顶点
                """
                graph = self.graph

                for _ in range(graph.num_of_vertex):
                    self.index += 1
                    if self.index < len(self.graph.info[self.v]):
                        return self.graph.info[self.v][self.index]
                return -1  # 找不到相邻顶点时返回-1

            def end(self):
                return self.index >= len(self.graph.info[self.v])

                # 直接返回所有相连接的节点列表
            def get_connected_vertex_list(self):
                self.index = -1
                res = []
                while not self.end():
                    tmp = self.next()
                    if tmp != -1:
                        res.append(tmp)
                return res

        return EdgeIterator(vertex)





