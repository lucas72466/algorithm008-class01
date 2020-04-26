#pragma once
#include<iostream>
#include<assert.h>


class MinHeap {
private:
	int capacity;
	int count;
	int* data;

	int parent(int k);
	int leftChild(int k);
	int rightChild(int k);
	void heapifyUp(int k);
	void heapifyDown(int k);
public:
	MinHeap(int capacity) {
		this->capacity = capacity;
		this->count = 0;
		this->data = new int[capacity];
	}

	MinHeap(vector<int>& vec) {  // heapify
		this->capacity = vec.size();
		this->data = new int[capacity];
		this->count = 0;

		for (auto& val : vec) {
			data[count++] = val;
		}

		for (int i = (count / 2) - 1; i >= 0; --i) {
			heapifyDown(i);
		}
	}

	~MinHeap() {
		delete[] data;
	}

	int getCapacity();
	int size();
	bool empty();
	void intsert(int val);
	void show();
	int extractMin();
	

};

int MinHeap::parent(int k) {
	return (k - 1) / 2;
}

int MinHeap::leftChild(int k) {
	return k * 2 + 1;
}

int MinHeap::rightChild(int k) {
	return k * 2 + 2;
}


int MinHeap::getCapacity() {
	return this->capacity;
}

int MinHeap::size() {
	return this->count;
}

bool MinHeap::empty() {
	return count == 0;
}

void MinHeap::heapifyUp(int k) {
	int const tmp = data[k];
	while (k>=1 && data[parent(k)]>tmp) {
		data[k] = data[parent(k)];
		k = parent(k);
	}
	data[k] = tmp;  // 确定最终位置后再进行赋值， 减少交换产生的开销
}

void MinHeap::heapifyDown(int k) {
	int const tmp = data[k];
	while (leftChild(k)<count)
	{
		int j = leftChild(k);
		if (j + 1 < count&&data[j] > data[j + 1])
			++j;

		if (tmp > data[j]) {
			data[k] = data[j];
			k = j;
		}
		else break;
	}
	data[k] = tmp;
}

void MinHeap::intsert(int val) {
	assert(this->count < this->capacity);
	data[count] = val;
	heapifyUp(count);
	++count;
}

void MinHeap::show() {
	for (int i = 0; i < count; ++i) {
		std::cout << data[i] << " ";
	}
	std::cout << std::endl;
}

int MinHeap::extractMin() {
	int ret = data[0];
	data[0] = data[count-1];
	--count;
	heapifyDown(0);
	return ret;
}