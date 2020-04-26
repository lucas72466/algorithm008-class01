"""
Kruskal算法： 开始时将所有边排序， 先找最短边，加入到生成树，如果不形成环就保留，形成就抛弃找下一小的边（借助并查集进行判断）
由边找点， 区别于Prim由点找边
Vyssitsky: 以任意顺序将边加入到生成树， 一旦形成环， 删除环中权值最大的边
"""
from MinHeap import MinHeap
from QuickUnion import QuickUnion


class KruskalMST:
    def __init__(self, graph):
        self.graph = graph
        self.mst = []  # 用于存储产生的最小生成树
        self.mst_weight = 0  # 用于存储最小生成树对应的权值
        self.pq = MinHeap()  # 用最小堆来作为优先队列

        self.Kruskal()

    @property
    def mst_(self):
        return self.mst

    @property
    def mst_weight_(self):
        return self.mst_weight

    def Kruskal(self):
        # 将所有边放入堆中
        for i in range(self.graph.num_of_vertex):
            connected_vertex_list = self.graph.get_edge_iterator(i).get_connected_vertex_list()
            for edge in connected_vertex_list:
                if edge.vertex_a > edge.vertex_b:  # 删除无向图中的重复边
                    self.pq.insert(edge)

        union_find = QuickUnion(len(self.pq.data))
        while not self.pq.is_empty() and len(self.mst) < self.graph.num_of_vertex - 1:

            edge = self.pq.extract_min()
            if union_find.is_connected(edge.vertex_a, edge.vertex_b):
                continue

            self.mst.append(edge)
            union_find.union_element(edge.vertex_a, edge.vertex_b)

        for edge in self.mst:
            self.mst_weight += edge.weight_



