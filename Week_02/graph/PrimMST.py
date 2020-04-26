"""
使用最小索引堆优化的Prim
"""
from IndexMinHeap import IndexMinHeap


class PrimMST:
    def __init__(self, graph):
        self.graph = graph  # 图的引用
        self.ipq = IndexMinHeap(graph.num_of_vertex)  # 用最小索引堆来作为优先队列， 存储对应边的权值
        self.edgeTo = [None for _ in range(graph.num_of_vertex)]  # 存储优先队列中对应的边
        self.marked = [False for _ in range(graph.num_of_vertex)]  # 用于标记该节点是否已经加入了最小生成树
        self.mst = []  # 用于存储产生的最小生成树
        self.mst_weight = 0  # 用于存储最小生成树对应的权值

        self.prim()

    @property
    def mst_(self):
        return self.mst

    @property
    def mst_weight_(self):
        return self.mst_weight

    def visit(self, vertex):
        """
        用于访问一个节点。
        将该节点的状态设为True, 表明已经加入到了最小生成树， 遍历该节点的边， 判断是否为横切边，如果是，
        则进入判断。如果该边的另外一个节点还没有加入到最小生成树， 则把权值加入到优先队列， 边的实例对象加入到
        edgeTo列表中
        """
        # assert not self.marked[vertex]
        self.marked[vertex] = True

        connected_vertex_list = self.graph.get_edge_iterator(vertex).get_connected_vertex_list()
        for edge in connected_vertex_list:
            vertex_e = edge.other(vertex)
            if not self.marked[vertex_e]:
                if self.edgeTo[vertex_e] is None:
                    self.ipq.insert(vertex_e, edge.weight_)
                    self.edgeTo[vertex_e] = edge
                elif self.edgeTo[vertex_e].weight_ > edge.weight_:
                    self.ipq.change(vertex_e, edge.weight_)
                    self.edgeTo[vertex_e] = edge

    def prim(self):
        """
        从初始节点开始进行访问（这里从0开始）。 当优先队列不为空， 取出堆顶元素， 对应边加入到最小生成树,
        再对这个节点进行访问
        """
        self.visit(0)
        while not self.ipq.is_empty():
            vertex = self.ipq.extract_min_index()
            #assert self.edgeTo[vertex] is not None
            self.mst.append(self.edgeTo[vertex])
            self.visit(vertex)

        for edge in self.mst:
            self.mst_weight += edge.weight_


