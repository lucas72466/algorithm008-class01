from DenseGraph import DenseGraph
from ReadGraph import read_graph
from SparseGraph import SparseGraph
from LazyPrimMST import LazyPrimMST
from PrimMST import PrimMST
from KruskalMST import KruskalMST
from Dijkstra import Dijkstra

if __name__ == '__main__':
    graph = SparseGraph(5, True)
    read_graph(graph, 'testG1.txt')
    tmp = Dijkstra(graph, 0)
    for i in range(5):
        tmp.show_path(i)
