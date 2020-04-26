"""
稠密图--邻接矩阵 不考虑平行边， 允许自环边
"""
import numpy as np


class DenseGraph:

    def __init__(self, num_of_vertex, directed):
        self.v = num_of_vertex  # 节点的数量 vertex
        self.e = 0  # 边的数量 edge 初始时默认没有边
        self.directed = directed  # 是否为有向图
        self.info = np.zeros((self.v, self.v), dtype=bool)  # 记录图的具体数据， 使用v*v大小的布尔型矩阵来表示

    @property
    def num_of_vertex(self):
        return self.v

    @property
    def edge(self):
        return self.e

    def add_edge(self, n, m):
        """
        向图中添加一个边
        :param n:  边的一个点
        :param m:  边的另一个点
        :return:   无返回值
        """

        assert self.v > n >= 0, '请输入正确的节点'
        assert self.v > m >= 0, '请输入正确的节点'

        if self.has_edge(n, m):  # 已经存在边就不进行操作
            return

        self.info[n, m] = True
        if not self.directed:
            self.info[m, n] = True

        self.e += 1

    def has_edge(self, n, m):
        """
        验证图中是否有从n到m的边
        :return:  布尔值
        """
        assert self.v > n >= 0, '请输入正确的节点'
        assert self.v > m >= 0, '请输入正确的节点'

        return self.info[n, m]

    def show(self):
        for i in range(self.v):
            print(i, end=': ')
            for j in range(self.v):
                print(int(self.info[i, j]), end=' ')
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
                self.index = -1  # 将初始索引设为-1

            def begin(self):
                """
                返回图中与顶点vertex相连接的第一个顶点， 内部调用自身的next() 方法
                """
                self.index = -1
                return self.next()

            def next(self):
                """
                返回图中与顶点vertex相连接的下一个顶点
                """
                graph = self.graph

                self.index += 1
                for _ in range(self.index, self.graph.num_of_vertex):
                    if graph.info[self.v, self.index]:
                        return self.index
                    self.index += 1

                return -1  # 找不到相邻顶点时返回-1

            # 查看是否已经迭代完了图G中与顶点v相连接的所有顶点
            def end(self):
                return self.index >= self.graph.num_of_vertex

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



