"""
图的深度优先遍历： 寻找联通分量
"""


class Component:

    def __init__(self, graph):
        self.graph = graph  # 图的引用
        self.c_count = 0  # 记录联通分量的个数
        self.v = graph.num_of_vertex
        self.id = [-1 for _ in range(self.v)]  # 记录每个节点属于哪一个联通分量
        self.visited = [False for _ in range(self.v)]  # 记录每个节点的访问状态 （不同于树的遍历， 图的遍历存在环， 需要记录状态）

        self.get_component()

    def get_component(self):
        for i in range(self.v):
            if not self.visited[i]:
                self.dfs(i)
                self.c_count += 1

    def dfs(self, vertex_f):
        self.visited[vertex_f] = True
        self.id[vertex_f] = self.count
        connected_vertex_list = self.graph.get_edge_iterator(vertex_f).get_connected_vertex_list()
        for vertex in connected_vertex_list:
            if not self.visited[vertex]:
                self.dfs(vertex)
    
    @property
    def count(self):
        return self.c_count
    
    def is_connected(self, n, m):
        assert self.v > n >= 0, '请输入正确的节点'
        assert self.v > m >= 0, '请输入正确的节点'
        
        return self.id[n] == self.id[m]


