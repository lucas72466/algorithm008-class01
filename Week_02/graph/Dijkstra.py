"""
Dijkstra 单源最短路径算法 （前提是图中不能有负权边）
"""
from IndexMinHeap import IndexMinHeap
from Edge import Edge
from Stack import Stack


class Dijkstra:
    def __init__(self, graph, initial_vertex):
        self.graph = graph  # 图的引用
        self.initial = initial_vertex  # 起始点
        self.v = graph.num_of_vertex  # 图的节点个数
        self.dist_to = [0 for _ in range(self.v)]  # dist_to[i] 存储从起始点到i的当前最短距离
        self.marked = [False for _ in range(self.v)]  # 标记数组, 在算法运行过程中标记节点i是否被访问
        self.from_ = [None for _ in range(self.v)]  # from_[i]记录最短路径中, 到达i点的边是哪一条
        self.ipq = IndexMinHeap(self.v)

        assert self.v > initial_vertex >= 0

        self.dijkstra()

    def shortest_path_to(self, vertex_t):
        return self.dist_to[vertex_t]

    def has_path_to(self, vertex_t):
        return self.marked[vertex_t]

    def shortest_path(self, vertex_t):
        assert self.v > vertex_t >= 0
        assert self.has_path_to(vertex_t)

        stack = Stack()
        tmp_edge = self.from_[vertex_t]
        while tmp_edge.vertex_a != self.initial:
            stack.push(tmp_edge)
            tmp_edge = self.from_[tmp_edge.vertex_a]
        stack.push(tmp_edge)

        res = []
        while not stack.is_empty():
            res.append(stack.pop())

        return res

    def show_path(self, vertex_t):
        assert self.v > vertex_t >= 0
        assert self.has_path_to(vertex_t)

        res = self.shortest_path(vertex_t)
        for edge in res:
            print(edge.vertex_a, end='-->')
            if edge == res[-1]:
                print(edge.vertex_b)

    def dijkstra(self):
        """
        """
        # 变量引用
        initial_v = self.initial
        ipq = self.ipq
        dist_to = self.dist_to

        # 开始对起始点进行初始化（到自己的距离为0， from的路径是自己指向自己的路径， 访问状态为true）.将起始点加入到最小索引堆当中。
        dist_to[initial_v] = 0
        self.from_[initial_v] = Edge(initial_v, initial_v, 0)
        ipq.insert(initial_v, dist_to[initial_v])
        self.marked[initial_v] = True

        while not ipq.is_empty():
            tmp_v = ipq.extract_min_index()
            self.marked[tmp_v] = True
            connected_vertex_list = self.graph.get_edge_iterator(tmp_v).get_connected_vertex_list()
            for edge in connected_vertex_list:
                other_vertex = edge.other(tmp_v)
                # 如果从s点到w点的最短路径还没有找到
                if not self.marked[other_vertex]:
                    # 如果w点以前没有访问过,
                    # 或者访问过, 但是通过当前的v点到w点距离更短, 则进行更新
                    if self.from_[other_vertex] is None or dist_to[tmp_v] + edge.weight_ < dist_to[other_vertex]:
                        dist_to[other_vertex] = dist_to[tmp_v] + edge.weight_
                        self.from_[other_vertex] = edge
                        if ipq.contain(other_vertex):
                            ipq.change(other_vertex, dist_to[other_vertex])
                        else:
                            ipq.insert(other_vertex, dist_to[other_vertex])


