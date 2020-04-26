"""
图的深度优先遍历： 寻路
还可以用于查看图中的环（针对有向图）
"""
from Stack import Stack


class Path:

    def __init__(self, graph, vertex):
        self.graph = graph  # 图的引用
        self.v = graph.num_of_vertex
        self.vertex = vertex
        self.from_ = [-1 for _ in range(self.v)]  # 记录是从哪个节点来的
        self.visited = [False for _ in range(self.v)]  # 记录每个节点的访问状态 （不同于树的遍历， 图的遍历存在环， 需要记录状态）

        self.dfs(vertex)

    def dfs(self, vertex_f):
        self.visited[vertex_f] = True
        connected_vertex_list = self.graph.get_edge_iterator(vertex_f).get_connected_vertex_list()
        for vertex_t in connected_vertex_list:
            if not self.visited[vertex_t]:
                self.from_[vertex_t] = vertex_f
                self.dfs(vertex_t)
    
    def has_path(self, vertex_t):
        assert self.v > vertex_t >= 0
        return self.visited[vertex_t]

    def path(self, vertex_t):
        assert self.v > vertex_t >= 0
        assert self.has_path(vertex_t)

        res = []
        tmp = Stack()

        i = vertex_t
        while self.from_[i] != -1:  # 通过from数组逆向查找到从s到w的路径, 存放到栈中
            tmp.push(i)
            i = self.from_[i]
        while not tmp.is_empty():  # 从栈中依次取出元素, 获得顺序的从s到w的路径
            res.append(tmp.pop())

        return res

    def show_path(self, vertex_t):
        path_list = self.path(vertex_t)
        print(self.vertex, end='-->')
        for vertex in path_list:
            print(vertex, end='')
            string = '-->' if vertex != path_list[-1] else '\n'
            print(string, end='')



