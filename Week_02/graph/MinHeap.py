"""
优先队列：出队顺序与入队顺序无关，和优先级相关
topK问题
实现二叉堆，二叉堆是一棵完全二叉树，堆中任意父节点的优先级总是高于子节点
由于完全二叉树这种良好性质，可以采用数组来实现二叉堆
"""
import random


class MinHeap:

    def __init__(self, *args):
        self.data = []
        self.count = 0
        for value in args:
            self.data.append(value)
            self.count += 1
        self.heapify()

    def size(self):
        return self.count

    @staticmethod
    def __parent(index):
        return int((index - 1) // 2)

    @staticmethod
    def __left_child(index):
        return int(index * 2 + 1)

    @staticmethod
    def __right_child(index):
        return int(index * 2 + 2)

    def heapify(self):
        for i in range(self.__parent(self.count - 1), -1, -1):
            self.__shift_down(i)

    def is_empty(self):
        return self.count == 0

    def __shift_up(self, k):
        while self.data[k] < self.data[self.__parent(k)] and k > 0:
            self.data[k], self.data[self.__parent(k)] = self.data[self.__parent(k)], self.data[k]
            k = self.__parent(k)

    def insert(self, element):
        self.data.append(element)
        self.count += 1
        self.__shift_up(self.count - 1)

    def __shift_down(self, k):
        while 2 * k + 1 < self.count:
            j = self.__left_child(k)
            if j + 1 <= self.count - 1 and self.data[j] > self.data[j + 1]:
                j = j + 1
            if self.data[k] > self.data[j]:
                self.data[k], self.data[j] = self.data[j], self.data[k]
                k = j
            else:
                break

    def extract_min(self):
        assert self.count > 0, 'There is not element in the heap'
        ret = self.data[0]
        self.data[0], self.data[self.count - 1] = self.data[self.count - 1], self.data[0]
        self.data.pop()
        self.count -= 1
        self.__shift_down(0)
        return ret

    def show(self):
        print(self.data)


def heap_sort(arr):
    min_heap = MinHeap(*arr)
    for i in range(min_heap.count):
        arr[i] = min_heap.extract_min()
    print(arr)


def right(func, arr):
    for i in range(len(arr) - 1):
        if not func(arr[i], arr[i + 1]):
            return False
    return True


def less(num1, num2):
    return True if num2 >= num1 else False


# 改进：原地堆排序

if __name__ == '__main__':
    nums = [random.randint(1, 10000) for _ in range(1000)]
    heap_sort(nums)
    print(right(less, nums))
