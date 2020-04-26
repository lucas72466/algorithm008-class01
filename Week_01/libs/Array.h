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
	// ���ι��캯�������д����С
	Array(int capacity) {
		data = new T[capacity];
		this->capacity = capacity;
	}
	// �޲ι��캯��
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

	// �������ָ��λ�����Ԫ��
	// ���������Ԫ�ص�˳�� ����Խ�indexλ�õ�Ԫ��ֱ�ӷŵ�ĩβ���ٸ�ֵ�� ��������Ŀ���
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

	// ����Ԫ�����ڵ������� ����������򷵻�-1
	int find(T element) {
		for (int i = 0; i < size; i++) {
			if (data[i] == element)
				return i;
		}
		return -1;
	}

	// ɾ��indexλ�õ�Ԫ�أ�������Ԫ�ط���
	/*�����ȼ�¼���Ѿ�ɾ�������ݡ�
	  ÿ�ε�ɾ�����������������ذ������ݣ�ֻ�Ǽ�¼�����Ѿ���ɾ����
	  ������û�и���ռ�洢����ʱ�������ٴ���ִ��һ��������ɾ������*/
	T remove(int index) {
		assert(index >= 0 && index < size);
		T ret = data[index];

		for (int i = index; i < size; i++) {
			data[index] = data[index + 1];
		}

		size--;
		data[size] = NULL;
		
		// lazy resize ���⸴�Ӷȵ���
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
