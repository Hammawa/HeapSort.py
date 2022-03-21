import math
class Heap:
    # initializes the heap with a given list and finds its size
    def __init__(self, A):
        self.heap = A
        self.heapSize = len(A)

    def isEmpty(self):
        '''Checks if list which represents the heap has zero elements'''
        if self.heapSize==0:
            return True
        else:
            return False

    def makeEmpty(self):
        '''Empties heap by clearing all elements in the heap'''
        self.heap.clear()

    def heapMax(self):
        '''Returns the maximum value of a given heap'''
        return self.heap[0]

    def parent(self, i):
        '''For some index i, the function returns the index of the parent node when applicable'''
        if i==0:
            return None
        else:
            return (i-1)//2

    def leftChild(self, i):
        '''For some index i, the function returns the index of the left child node when applicable'''
        if 2*i+1 > self.heapSize-1:
            return None
        else:
            return (2*i+1)

    def rightChild(self, i):
        '''For some index i, the function returns the index of the right child node when applicable'''
        if 2*i+2 > self.heapSize-1:
            return None 
        else:
            return (2*i+2)

    def Swap(self, i, largest):
        '''Takes in the index of two items in the heap and swaps them'''
        self.heap[i], self.heap[largest] =  self.heap[largest] ,  self.heap[i]

    def maxHeapify(self, i):
        '''Takes in an index i, compares the elementt at index i to its left and right child before swapping them accordingly to create a proper heap data structure '''
        l = self.leftChild(i)
        r = self.rightChild(i)
        
        
        if l==None:
            largest = i
        elif l < self.heapSize and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r==None:
            largest = largest
        elif r < self.heapSize and self.heap[r] > self.heap[largest] and self.heap[r] > self.heap[l]:
            largest = r 
        # when a new value for largest is found it is swapped with the old value for largest 
        if largest != i:
            self.Swap(i, largest)
            self.maxHeapify(largest)
            

    def buildMaxHeap(self):
        '''Builds a heap using the maxHeapify function'''
        for i in range((self.heapSize//2)-1, -1, -1):
            self.maxHeapify(i)

    def extractMax(self):
        '''Returns the maximum value of a heap and deletes it from the heap'''
        if self.heapSize < 1:
            print("error “heap underflow”")
        maxs = self.heap[0]
        self.heap[0] = self.heap[self.heapSize-1]
        self.heapSize = self.heapSize - 1
        self.maxHeapify(0)
        return maxs

    def deleteNode(self, i):
        '''Takes in i and returns the value of the node at index i before deleting it'''
        self.heapSize = self.heapSize-1
        return self.heap[i], self.heap.remove(self.heap[i])

    def insertNode(self, key):
        '''Takes a new value called key and inserts it into the heap'''
        self.heapSize = self.heapSize+1
        self.heap.append(-math.inf)
        self.increaseNodeKey(self.heapSize-1, key)

    def increaseNodeKey(self, i, key):
        '''increase node’s i key by given key'''
        if key < self.heap[i]:
            print("error(New key must be greater than current key)")
        self.heap[i]=key
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.Swap(i, self.parent(i))
            i = self.parent(i)
                                  

    def printHeap(self):
        '''Print heap elements'''
        print(self.heap)
 
    def heapSort(self):
        '''Uses the buildMaxHeap, Swap and maxHeapify functions in order to sore the list in ascending order '''
        self.buildMaxHeap()
        for i in range(self.heapSize-1, 0, -1):
            self.Swap(0, i)
            self.heapSize = self.heapSize - 1
            self.maxHeapify(0)
            
            
def main():
    A = [12, 3, 1500000, 5, 81, 3, 6, 150000000001]
    print("The list A")
    print(A)
    print(" ")
    h = Heap(A)
    #testing the heap function
    h.buildMaxHeap()
    print("The heap of list A")
    h.printHeap()
    print(" ")
    #testing the parent, leftChild and rightChild functions at index 2
    a = 2
    b = h.parent(a)
    c = h.leftChild(a)
    d = h.rightChild(a)
    print("The parent, left child, and right child at index 2")
    print("Parent:", h.heap[b])
    print("Left Child:", h.heap[c])
    print("Right Child:", h.heap[d])
    h.printHeap()
    print(" ")    
    #testing the deleteNode function
    h.deleteNode(1)
    print("Deletes the node at index 1")
    h.printHeap()
    print(" ")
    #testing the insertNode function
    h.insertNode(81)
    print("Inserts the value 81 into the heap")
    h.printHeap()
    print(" ") 
    #testing the heapSort function
    h.heapSort()
    print("Sorts the Heap")
    h.printHeap()
    print(" ")     
main()