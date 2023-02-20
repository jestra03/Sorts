# Data Structure
# Max Heap [Priority Queue]

class MaxHeap:
    def __init__(self, capacity=50):
        self.capacity = capacity  # set capacity
        self.heap = [0] * (capacity + 1)  # initialize array
        self.size = 0  # set item counter
    # Constructor creating an empty heap of user-defined capacity
    # The capacity is 50 by default
    # index 0 is disregarded to allow for better arithmetic when percolating

    def enqueue(self, item):
        if self.is_full():
            return False
        self.size += 1
        self.heap[self.size] = item
        self.perc_up(self.size)
        return True
    # inserts "item" into the heap
    # returns true if successful
    # returns false if there is no room in the heap
    # "item" can be any primitive or ***object*** that can be compared with other items using the < operator
    # Should call perc_up

    def peek(self):
        if self.is_empty():
            return None
        else: return self.heap[1]
    # returns max
    # returns None if heap is empty

    def dequeue(self):
        if self.is_empty():
            return None
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]  # replace root with last leaf element
        self.size -= 1
        self.perc_down(1)  # rearrange binary tree and perc down 1 to right position
        return max
    # returns max and removes it from the heap
    # returns None if the heap is empty
    # calls perc_down to maintain heap structure

    def contents(self):
        return self.heap[1:self.size + 1]
    # returns the elements of the array as it is stored in the heap

    def heapify(self, arr):
        self.size = len(arr)
        if self.capacity < len(arr):
            self.capacity = len(arr)
        arr = [None] + arr
        self.heap = arr  # previous heap discarded
        idx = 1
        while True:
            if idx * 2 > self.size or idx * 2 + 1 > self.size:
                last_parent = idx
                break
            else:
                idx += 1
        while last_parent > 1:  # bottom up construction
            self.perc_down(last_parent)
            last_parent -= 1
        self.perc_down(1)
        while len(self.heap) < self.capacity + 1:  # restore array capacity
            self.heap.append(0)
    # builds a new heap from a new array
    # Bottom-Up construction

    def is_empty(self):
        return self.size == 0
    # returns True if the heap is empty, false otherwise

    def is_full(self):
        return self.size == self.capacity
    # returns True if the heap is full, false otherwise

    def get_capacity(self):
        return self.capacity
    # returns maximum number of entries the heap can hold

    def get_size(self):
        return self.size
    # returns the number of "items" in the array

    def perc_down(self, i):
        while i * 2 <= self.size:  # within bounds [there is child element]
            if self.is_leftChild(i) and not self.is_rightChild(i):
                if self.heap[i] < self.heap[i * 2]:
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            elif self.is_leftChild(i) and self.is_rightChild(i):
                if self.heap[i] < self.heap[i*2] or self.heap[i] < self.heap[(i*2) + 1]:
                    if self.heap[i*2] > self.heap[(i*2) + 1]:
                        self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                        i = i * 2
                    else:
                        self.heap[i], self.heap[(i*2) + 1] = self.heap[(i*2) + 1], self.heap[i]
                        i = i * 2 + 1
                else:
                    i = i * 2
    # perc_down moves the element stored at that location to its proper place in the heap
    # elements are rearranged during perc_down to maintain heap structure

    def is_leftChild(self, i):
        return i * 2 <= self.size

    def is_rightChild(self, i):
        return i * 2 + 1 <= self.size

    def perc_up(self, i):
        while i // 2 > 0:  # within bounds
            if self.heap[i] > self.heap[i // 2]:  # if child is greater than parent
                temp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = temp
            i = i // 2
    # perc_up moves the element stored at that location to its proper place in the heap while rearranging elements

    def heap_sort(self, alist):
        self.heapify(alist)  # replace current heap and build MaxHeap of given list
        idx = self.size
        sorted_lst = []
        while idx >= 0:  # dequeue in order [Max to Min]
            sorted_lst.append(self.dequeue())
            idx -= 1
        idx1 = len(sorted_lst) - 2  # start from end of max to min list
        idx2 = 0  # start at beginning for alist
        while idx1 >= 0:
            alist[idx2] = sorted_lst[idx1]  # mutate given list using reverse iteration of sorted list
            idx1 -= 1
            idx2 += 1
    # perform heap sort on input array in ascending order
    # This method will discard the current contents of the heap, build a new heap using the items in new arr
    # mutate arr to put the items in ascending order


"""
    Heap Sort
    - Max heap is created with new arr (O(nlog(n)))
    - dequeues Max heap for sorted array (descend order) (O(n))
    - reverse array (ascending order) (O(n))
     
    """
