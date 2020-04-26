from DenseGraph import DenseGraph
from SparseGraph import SparseGraph
from Component import Component
from ReadGraph import read_graph
from Path import Path
from ShortestPath import ShortestPath


if __name__ == '__main__':
    d_graph = DenseGraph(7, False)
    read_graph(d_graph, 'testG2.txt')
    d_graph.show()
    # component = Component(s_graph)
    path = ShortestPath(d_graph, 0)
    path.show_path(6)
