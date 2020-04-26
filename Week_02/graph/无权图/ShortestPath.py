"""
图的广度优先遍历： 寻找最短路径
"""
from Queue import Queue
from Stack import Stack


class ShortestPath:

    def __init__(self, graph, vertex):
        self.graph = graph  # 图的引用
        self.v = graph.num_of_vertex
        self.vertex = vertex
        self.from_ = [-1 for _ in range(self.v)]  # 记录是从哪个节点来的
        self.visited = [False for _ in range(self.v)]  # 记录每个节点的访问状态 （不同于树的遍历， 图的遍历存在环， 需要记录状态）
        self.order = [-1 for _ in range(self.v)]  # 记录当前点的层序

        self.queue = Queue()
        self.bfs(self.queue)

    def bfs(self, queue):
        queue.en_queue(self.vertex)
        self.visited[self.vertex] = True
        self.order[self.vertex] = 0
        while not queue.is_empty():
            vertex_f = queue.de_queue()
            connected_vertex_list = self.graph.get_edge_iterator(vertex_f).get_connected_vertex_list()
            for vertex in connected_vertex_list:
                if not self.visited[vertex]:
                    queue.en_queue(vertex)
                    self.visited[vertex] = True
                    self.from_[vertex] = vertex_f
                    self.order[vertex] += self.order[vertex_f] + 1

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

    def length(self, vertex_t):
        assert self.v > vertex_t >= 0
        return self.order[vertex_t]

