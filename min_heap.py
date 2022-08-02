# Name: Tristan Pereira
# OSU Email: pereirtr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5 - MinHeap Implementation
# Due Date:08/01/2022
# Description: min_heap.py implements a priority queue ADT by using a heap data structure built on a dynamic array.
#multiple functions are created to manipulate the nodes inside the heap.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        '''Adds a node to the correct spot on the heap.'''

        self._heap.append(node)
        i = self._heap.length()-1
        p = (i-1)//2 #parent node
        #iterate from the end of the Heap and check for minimum value
        while(i> 0 and self._heap[i]<self._heap[p]):
            temp = self._heap[i]
            self._heap[i] = self._heap[p]
            self._heap[p] = temp
            i = p
            p = (i-1)//2

    def is_empty(self) -> bool:
        '''is_empty returns True if the Heap is empty and False otherwise.'''

        if self._heap.is_empty():
            return True
        else:
            return False

    def get_min(self) -> object:
        '''get_min returns the node with the minimum value, if the heap is empty it raises an Exception.'''

        if self._heap.is_empty():
            raise MinHeapException
        else:
            return self._heap[0]

    def remove_min(self) -> object:
        '''remove_min function removes the minimum value in the Heap and returns that node. If the heap is empty it raises an exception.'''

        if self._heap.is_empty():
            raise MinHeapException

        min = self._heap[0]
        #switch first and last
        self._heap[0], self._heap[self._heap.length() - 1] = self._heap[self._heap.length() - 1], self._heap[0]
        self._heap.pop() # remove last

        _percolate_down(self._heap, 0, self._heap.length()) #Then percolate down once.
        return min

    def build_heap(self, da: DynamicArray) -> None:
        '''build_heap function takes in a dynamic array and builds a heap from the unordered elements. '''

        heap2 = DynamicArray()

        for i in da:
            heap2.append(i)
        self._heap = heap2

        i = (da.length())//2 - 1 #Last subtree
        while(i>=0):
            _percolate_down(self._heap, i, self._heap.length()) #percolate every index
            i -= 1

    def size(self) -> int:
        '''size function returns the length of the Heap.'''

        return self._heap.length()

    def clear(self) -> None:
        '''clear function emptys the Heap.'''
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    '''heapsort function takes in a dynamic array as a parameter,
    creates a new heap, and then continuously sorts it by percolating down. '''

    k = da.length()//2 - 1

    while (k>=0):
        _percolate_down(da,k,da.length())
        k-=1

    k = da.length()-1
    while(k>=0):
        da[k], da[0] = da[0], da[k]
        _percolate_down(da,0, k)
        k-=1

def _percolate_down(da: DynamicArray, parent: int, size: int) -> None:
    '''_percolate_down function iterates through the heap by comparing values of the current node to its children, then contiously switching until its at the correct place
    in the Heap.'''

    i = parent

    while (True):
        min = i
        ch1 = 2 * i + 1
        ch2 = 2 * i + 2
        if (ch1 <= size - 1 and da[i] > da[ch1]):
            min = ch1

        if ch2 <= size - 1 and da[min] > da[ch2]:
            min = ch2

        if min == i: #no comparison to be made/correct spot
            break

        da[i], da[min] = da[min], da[i]
        i = min










# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
