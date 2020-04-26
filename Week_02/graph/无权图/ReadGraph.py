from DenseGraph import DenseGraph
from SparseGraph import SparseGraph


def read_graph(graph, filename):
    """
    将文件中的数据读出并初始化图
    """
    with open(filename, 'r') as f:
        tmp = f.readline().strip().split(' ')  # 读出行首顶点数和边数
        v = int(tmp[0])
        e = int(tmp[1])
        assert v == graph.num_of_vertex, '文件与图节点数不相符'
        for line in f.readlines():
            tmp = line.strip().split(' ')
            n, m = int(tmp[0]), int(tmp[1])

            assert v > n >= 0, '请输入正确节点数'
            assert v > m >= 0, '请输入正确节点数'

            graph.add_edge(n, m)



