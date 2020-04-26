#pragma once
#include<iostream>

using namespace std;

// 单向链表的实现
template<typename T>
class LinkedList {
private:
	class Node {
	public:
		T element;
		Node* next;

		Node(T element=NULL, Node* next=nullptr) {
			this->element = element;
			this->next = next;
		}
	};

	Node dummyHead;
	int size;

	void clear() {
		Node *cur, *tmp;
		cur = dummyHead.next;
		while (cur != nullptr) {
			tmp = cur;
			cur = cur->next;
			delete cur;
		}
		dummyHead.next = nullptr;
		size = 0;
	}

public:

	LinkedList() {
		dummyHead = Node();
		size = 0;
	}

	~LinkedList() {
		clear();
	}

	int getSize() {
		return size;
	}

	bool isEmpty() {
		return size==0;
	}

	void insert(int index, T element) {
		assert(index >= 0 && index <= size);

		Node* node = new Node(element);
		Node* prev = &dummyHead;
		for (int i = 0; i < index; i++) {
			prev = prev->next;
		}
		node->next = prev->next;
		prev->next = node;
		size++;	
	}

	void insertLast(T element) {
		insert(size, element);
	}

	void insertFirst(T element) {
		insert(0, element);
	}

	Node* remove(int index) {
		assert(index >= 0 && index < size);

		Node* prev = &dummyHead;
		for (int i = 0; i < index; i++) {
			prev = prev->next;
		}
		Node* ret = prev->next;
		prev->next = ret->next;
		ret->next = nullptr;
		size--;
		return ret;
	}

	Node* removeFirst() {
		return remove(0);
	}

	Node* removeLast() {
		return remove(size - 1);
	}

	void set(int index, T element) {
		assert(index >= 0 && index <= size);

		Node* cur = dummyHead.next;
		for (int i = 0; i < index; i++) {
			cur = cur->next;
		}
		cur->element = element;
	}

	bool contain(T element) {
		Node* cur = dummyHead.next;
		while (cur!=nullptr){
			if (cur->element == element)
				return true;
			cur = cur->next;
		}
		return false;
	}

	void print() {
		if (size == 0) {
			cout << "NULL" << endl;
			return;
		}
		Node* cur = dummyHead.next;
		while (cur->next != nullptr) {
			cout << cur->element << "->";
			cur = cur->next;
		}

		cout << cur->element << endl;
	}



};

