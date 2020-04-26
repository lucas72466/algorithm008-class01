"""
从起始节点开始，作为切分的一部分，
剩下的节点作为切分的另一部分。找到横切边中权值最小的那一个（使用最小堆实现），
如果横切边另外一边没有被加入最小生成树，那么就选取这条横切边并将该节点变为最小生成树
以此类推
"""
from MinHeap import MinHeap


class LazyPrimMST:

    def __init__(self, graph):
        self.graph = graph  # 图的引用
        self.pq = MinHeap()  # 用最小堆来作为优先队列
        self.marked = [False for _ in range(graph.num_of_vertex)]  # 用于标记该节点是否已经加入了最小生成树
        self.mst = []  # 用于存储产生的最小生成树
        self.mst_weight = 0  # 用于存储最小生成树对应的权值

        self.lazy_prim()

    @property
    def mst_(self):
        return self.mst

    @property
    def mst_weight_(self):
        return self.mst_weight

    def lazy_prim(self):
        """
        从初始节点开始（这里选取0）访问临边寻找横切边， 从当前优先队列中取出最小的边（要进行一次横切边判断），
        将此边加入到最小生成树， 然后访问该横切边未加入到最小生成树的节点。最后累加最小生成树的权值
        """
        self.visit(0)
        while not self.pq.is_empty():
            tmp = self.pq.extract_min()
            # 虽然加入的时候判断了一次横切边，但在取出之前可能节点状态发生了改变， 还需要再一次判断
            if self.marked[tmp.vertex_a] == self.marked[tmp.vertex_b]:
                continue

            self.mst.append(tmp)
            if not self.marked[tmp.vertex_a]:
                self.visit(tmp.vertex_a)
            else:
                self.visit(tmp.vertex_b)

        for edge in self.mst:
            self.mst_weight += edge.weight_

    def visit(self, vertex):
        """
        用于访问一个节点的相邻节点， 如果该相邻节点还没有加入最小生成树，那么这条边就是一个
        横切边（即潜在的最小生成树的边）， 将其加入到优先队列中, 并且该节点加入最小生成树
        """
        assert not self.marked[vertex]
        self.marked[vertex] = True

        connected_vertex_list = self.graph.get_edge_iterator(vertex).get_connected_vertex_list()
        for edge in connected_vertex_list:
            if not self.marked[edge.other(vertex)]:
                self.pq.insert(edge)

