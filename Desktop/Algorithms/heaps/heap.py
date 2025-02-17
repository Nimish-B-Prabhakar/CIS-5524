class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = (
                self.heap[index],
                self.heap[parent_index],
            )
            self._heapify_up(parent_index)

    def bubble_up(self, index=None):
        if index is None:
            index = len(self.heap) - 1  # Default to last element

        while index > 0:
            parent_index = (index - 1) // 2  # Get parent index

            if self.heap[parent_index] < self.heap[index]:  # Max heap condition
                self.heap[parent_index], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent_index],
                )  # Swap
                index = parent_index  # Move up
            else:
                break  # Stop if heap property is satisfied

    def bubble_up_improved(self, index=None):
        if index is None:
            index = len(self.heap) - 1  # Default to last element

        current = self.heap[index]  # Store the element to be moved

        while index > 0:
            parent_index = (index - 1) // 2  # Compute parent index

            if self.heap[parent_index] < current:  # Compare priority
                self.heap[index] = self.heap[parent_index]  # Shift parent down
                index = parent_index  # Move index up
            else:
                break  # Stop if heap property is satisfied

        self.heap[index] = current  # Place current in correct position

    def get_max(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        maxElement = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return maxElement
        lastElement = self.heap[len(self.heap) - 1]
        self.heap[0] = lastElement
        self._heapify_down(0)
        return maxElement

    def _heapify_down(self, index):
        left_Child_Index = index * 2 + 1
        right_Child_Index = index * 2 + 2
        largest = index

        if (
            left_Child_Index < len(self.heap)
            and self.heap[left_Child_Index] > self.heap[largest]
        ):
            largest = left_Child_Index

        if (
            right_Child_Index < len(self.heap)
            and self.heap[right_Child_Index] > self.heap[largest]
        ):
            largest = right_Child_Index

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)

    # Note: code can be improved by using dictionary for as an index map instead of linear
    # iteration on array
    def update_element(self, current_val, updated_val):
        # Find the index of the element to update
        for index, element in enumerate(self.heap):
            if current_val == element:
                # Update the value in the heap
                self.heap[index] = updated_val

                # Check if we should bubble up or push down
                parent_index = (index - 1) // 2  # Compute parent index

                if index > 0 and self.heap[parent_index] < self.heap[index]:
                    self._heapify_up(index)  # Bubble up if needed
                else:
                    self._heapify_down(index)  # Push down if needed

                break  # Stop after updating

    def heapify(self, arr):
        """Transforms an unordered array into a valid heap in O(n) time."""
        self.heap = arr  # Assume self.heap stores the heap array
        last_non_leaf = (len(arr) // 2) - 1  # Index of last non-leaf node

        # Start from last non-leaf node and push down each node to maintain heap property
        for index in range(last_non_leaf, -1, -1):  # Process from right to left
            self._heapify_down(index)

    def heap_sort(self):
        n = len(self.heap)

        # Step 1: Build the max heap (heapify the array)
        last_non_leaf = (n // 2) - 1
        for index in range(last_non_leaf, -1, -1):  # Bottom-up heapification
            self._heapify_down(index)

        # Step 2: Extract elements from the heap
        for end in range(n - 1, 0, -1):
            # Swap root (max element) with the last element
            self.heap[0], self.heap[end] = self.heap[end], self.heap[0]

            # Heapify down on the reduced heap (excluding last element)
            self._heapify_down(0)  # Always call on root
