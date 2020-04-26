"""
基于快速Find的并查集：使用数组来存储，存储的是组别，如此查询速度非常快，但是合并集合需要遍历数组效率低下
基于快速Union的并查集： 形式上是一棵由子节点指向父节点的特殊的树结构
基于size，rank进行优化
路径压缩
"""


class QuickUnion:

    def __init__(self, count):
        self.parent = [-1 for i in range(count)]
        # self.size = []
        self.rank = [-1 for i in range(count)]  # 表示以此节点为根的树的高度
        self.count = count
        for i in range(count):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, p):
        assert 0 <= p < self.count
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]  # 路径压缩
            p = self.parent[p]
        return p
        # if p != self.parent[p]:
        #     self.parent[p] = self.find(self.parent[p])   # 最佳路径压缩， 逻辑上最优，实际运行递归造成的开销会有所影响
        # return self.parent[p]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union_element(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        # 基于rank的优化
        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1

if __name__ == '__main__':
    uf = QuickUnion(10)
    uf.union_element(0, 9)
    uf.union_element(2, 9)
    print(uf.is_connected(0,2))
    print(uf.is_connected(0,9))
    print(uf.is_connected(9,2))
    print(uf.parent)
    print(uf.rank)