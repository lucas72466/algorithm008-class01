#pragma once
#include<iostream>
#include<assert.h>

using namespace std;

template<typename T>
class Array {
private:
	int capacity;
	int size = 0;
	T* data=nullptr;
	
public:
	// 带参构造函数，自行传入大小
	Array(int capacity) {
		data = new T[capacity];
		this->capacity = capacity;
	}
	// 无参构造函数
	Array() {
		data = new T[10];
		this->capacity = 10;
	}

	~Array()
	{
		delete[] data;
	}


	int getCapacity() {
		return this->capacity;
	}

	int getSize() {
		return this->size;
	}

	bool isEmpty() {
		return size == 0;
	}

	void addLast(T element) {
		add(size, element);
	}

	void addFirst(T element) {
		add(0, element);
	}

	// 向数组的指定位置添加元素
	// 如果不关心元素的顺序， 则可以将index位置的元素直接放到末尾，再赋值， 避免大量的拷贝
	void add(int index, T element) {
		assert(index>=0 && index <=size);

		if (size == capacity) {
			resize(2 * capacity);
		}
		
		for (int i = size - 1; i > index; i++) {
			data[i] = data[i - 1];
		}
		data[index] = element;
		size++;
	}

	void resize(int const capacity) {
		T* newData = new T[capacity];
		for (int i = 0; i < size; i++) {
			newData[i] = data[i];
		}
		delete[] data;
		data = newData;
		newData = nullptr;
	}

	T get(int index) {
		assert(index >= 0 && index <= size);

		return data[index];
	}

	void set(int index, T element) {
		assert(index >= 0 && index <= size);

		data[index] = element;
	}

	bool contains(T element) {
		for (int i = 0; i < size; i++) {
			if (data[i] == element)
				return true;
		}
		return false;
	}

	// 查找元素所在的索引， 如果不存在则返回-1
	int find(T element) {
		for (int i = 0; i < size; i++) {
			if (data[i] == element)
				return i;
		}
		return -1;
	}

	// 删除index位置的元素，并将该元素返回
	/*可以先记录下已经删除的数据。
	  每次的删除操作并不是真正地搬移数据，只是记录数据已经被删除。
	  当数组没有更多空间存储数据时，我们再触发执行一次真正的删除操作*/
	T remove(int index) {
		assert(index >= 0 && index < size);
		T ret = data[index];

		for (int i = index; i < size; i++) {
			data[index] = data[index + 1];
		}

		size--;
		data[size] = NULL;
		
		// lazy resize 避免复杂度的震荡
		if (size <= capacity / 4 && capacity / 2 != 0) {
			resize(capacity / 2);
		}
		return ret;
	}

	T removeLast() {
		return remove(size - 1);
	}

	T removeFirst() {
		return remove(0);
	}

	void showArray() {
		cout << "Array " << "(";
		for (int i = 0; i < size; i++) {
			cout << data[i] << " ";
		}
		cout << ")"<<endl;
	}
};
