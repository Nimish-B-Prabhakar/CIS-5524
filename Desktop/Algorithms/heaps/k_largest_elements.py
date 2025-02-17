from heap import Heap


def find_k_largest_elements_using_heapify(heap, k):
    k_largest_element_arr = []

    # Build Max Heap (Heapify)
    last_non_leaf = (len(heap.heap) // 2) - 1
    for index in range(last_non_leaf, -1, -1):
        heap._heapify_down(index)

    # Extract k largest elements
    for i in range(k):
        k_largest_element_arr.append(heap.heap[0])  # Root is the max element
        heap.heap[0] = heap.heap[-1]  # Move last element to root
        heap.heap.pop()  # Remove last element from heap
        heap._heapify_down(0)  # Restore heap property

    return k_largest_element_arr


def find_k_largest_elements_using_minheap(self, arr, k):
    # Initialize the heap
    heap = Heap()

    # Iterate through the array and maintain a heap of size k
    for el in arr:
        if len(heap.heap) < k:
            heap.insert(el)
        else:
            # If heap is full and current element is larger than root (smallest in heap)
            if heap.get_max() < el:
                heap.extract_max()
                heap.insert(el)

    # At the end, the heap will contain the top K largest elements
    return heap.heap


"""
1. Heapify Approach:
Time Complexity:

Building the Max Heap:
Constructing the heap takes O(n) time, where n is the size of the array. This is because 
when you build a heap from an unsorted array, you start heapifying from the last non-leaf
node and process each node in a bottom-up manner, which takes linear time.

Extracting the K largest elements:
Extracting the root element (max) from the heap and then reheapifying takes O(logn) for 
each of the k extractions. Therefore, the extraction part takes O(klogn).

Total Time Complexity:

                O(n)+O(klogn)=O(n+klogn)
                
                
Use Case: When the size k is close to n, the heapify approach can be slower, as it requires
O(n) for heap construction, making it inefficient when k≪n.               
"""

"""
2. Min-Heap Approach::
Time Complexity:

Building the Min-Heap with K Elements:
The first k elements are inserted into the Min-Heap, which takes O(klogk).

Processing Remaining Elements:
For each of the remaining n-k elements, we check if the current element is greater than 
the root of the Min-Heap (which is the smallest of the largest 
k elements). If so, we replace the root and reheapify. Each insertion operation 
(involving replacing and reheapifying) takes 
O(logk) time, so processing the remaining elements takes O((n-k)logk).

Total Time Complexity:

                O(klogk)+O((n-k)logk)=O(nlogk)
                
Use Case: This is ideal when k≪n, and you only need to keep track of the largest k elements.
It offers better performance than the heapify approach, especially when the number of 
elements to be tracked is small relative to the size of the array.                
"""
