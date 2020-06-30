#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Node:
    '''
    创建一个节点
    '''
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderList:

    def __init__(self):
        self.head = None

    def add(self,item):
        '''
        在表头添加一个节点
        '''
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        '''
        返回链表的长度
        '''
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        '''
        查找链表中是否存在某个数据
        '''
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        '''
        移除链表中第一个被找到的对应节点数据
        '''
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self,item):
        '''在链表的末尾添加一个节点数据'''
        current = self.head
        while current != None:
            if current.getNext() == None:
                temp = Node(item)
                current.setNext(temp)
                break
            current = current.getNext()

    def index(self,item):
        '''
        返回链表中第一个找到的节点数据的下标(默认从1开始，下同)
        '''
        current = self.head
        count = 0
        found = False
        while not found :
            if current.getData() == item:
                found = True
            count += 1
            current = current.getNext()
        return count

    def insert(self,pos,item):
        '''将链表中对应下标的节点数据更改'''
        current = self.head
        previous = None
        try:
            for i in range(pos-1):
                previous = current
                current = current.getNext()
            temp = Node(item)
            temp.setNext(current)
            previous.setNext(temp)

        except AttributeError:
            self.add(item)

    def pop(self,pos = None):
        '''
        pop()：移除链表中的最后一个节点数据
        pop(pos)：移除链表中指定位置的节点数据
        '''
        current = self.head
        previous = None
        if pos == None:
            for i in range(self.size()-2):
                current = current.getNext()
            if self.size() != 1:
                current.setData(None)
                current.setNext(None)
            elif self.size() == 1:
                self.__init__()
        elif pos == 2:
            previous = current
            current = current.getNext()
            previous.setNext(current.getNext())
        elif pos == 1:
            self.head = current.getNext()

    def isEmpty(self):
        '''
        返回链表是否为空
        '''
        return self.head == None



a = UnorderList()
a.add(1)
# a.add(2)
# a.add(4)
# a.insert(1,5)
# print(a.index(1))
# print(a.index(2))
# print(a.index(4))
# print(a.index(5))
a.pop()
print(a.size())
# print(a.search(1))

