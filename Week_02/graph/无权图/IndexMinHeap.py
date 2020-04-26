"""
索引堆
使用的场景：
改进：使用反向查找表
indexes 表示的是堆的顺序，即index【i】表示的是在i这个位置所对应的元素在data中的索引
而reverse则表示的是data中对应索引索引在堆中的位置，所以叫反向查找表

使用堆实现多路归并排序； d叉堆； 赋值操作替代交换操作
"""
import random


class IndexMinHeap:

    def __init__(self, capacity,  *args):
        self.data = []  # 最小索引堆中的数据
        self.count = 0  #
        self.indexes = []  # 最小索引堆中的索引
        self.reverse = []  # 最小索引堆中的反向索引, reverse[i] = x 表示索引i在x的位置
        self.capacity = capacity
        if args is not None:
            for value in args:
                self.data.append(value)
                self.indexes.append(self.count)
                self.reverse.append(self.count)
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
        data = self.data
        indexes = self.indexes
        reverse = self.reverse
        parent = self.__parent

        # 索引堆中, 数据之间的比较根据data的大小进行比较, 但实际操作的是索引
        while data[indexes[k]] < data[indexes[parent(k)]] and k > 0:
            indexes[k], indexes[parent(k)] = indexes[parent(k)], indexes[k]
            reverse[indexes[parent(k)]] = parent(k)
            reverse[indexes[k]] = k
            k = parent(k)

    def insert(self, element):
        # 这里的实现其实更类似于append
        assert self.count <= self.capacity, 'too long'

        self.data.append(element)
        self.indexes.append(self.count)
        self.reverse.append(self.count)
        self.count += 1
        self.__shift_up(self.count - 1)

    def __shift_down(self, k):
        data = self.data
        indexes = self.indexes
        reverse = self.reverse

        while 2 * k + 1 < self.count:
            j = self.__left_child(k)
            if j + 1 < self.count and data[indexes[j]] > data[indexes[j + 1]]:
                j += 1
            if data[indexes[k]] > data[indexes[j]]:
                indexes[k], indexes[j] = indexes[j], indexes[k]
                reverse[indexes[k]] = k
                reverse[indexes[j]] = j
                k = j
            else:
                break

    def extract_min(self):
        assert self.count > 0, 'There is not element in the heap'

        indexes = self.indexes

        ret = self.data[indexes[0]]
        indexes[0], indexes[self.count - 1] = indexes[self.count - 1], indexes[0]  # 注意这里不需要维护data数组，我们默认索引堆使用是不增加新元素的
        self.reverse[indexes[self.count - 1]] = -1  # 逻辑删除
        indexes.pop()
        self.count -= 1

        if self.count:
            self.reverse[indexes[0]] = 0
            self.__shift_down(0)
        return ret

    def extract_min_index(self):
        assert self.count > 0

        data = self.data
        indexes = self.indexes

        ret = indexes[0]
        indexes[0], indexes[self.count - 1] = indexes[self.count - 1], indexes[0]  # 注意这里不需要维护data数组，我们默认索引堆使用是不增加新元素的
        indexes.pop()
        self.count -= 1
        self.reverse[indexes[self.count - 1]] = -1  # 逻辑删除
        if self.count:
            self.reverse[indexes[0]] = 0
            self.__shift_down(0)
        return ret

    def get_max(self):
        assert self.count > 0
        return self.data[self.indexes[0]]

    def get_max_index(self):
        assert self.count > 0
        return self.indexes[0]

    def get_item(self, index):
        return self.data[index]

    def change(self, index, element):

        self.data[index] = element

        j = self.reverse[index]
        self.__shift_up(j)
        self.__shift_down(j)

    def contain(self, index):
        return self.reverse[index] != -1

    def show(self):
        for i in self.indexes:
            print(self.data[i])


def test():
    def heap_sort(capacity, arr):
        min_heap = IndexMinHeap(capacity, *arr)
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

    nums = [random.randint(1, 10000) for _ in range(1000)]

    heap_sort(1000, nums)
    print(right(less, nums))


if __name__ == '__main__':
    test()
