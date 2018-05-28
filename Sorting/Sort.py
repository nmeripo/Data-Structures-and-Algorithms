import random

class Sort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.left = 0
        self.right = self.n - 1

        
    """
    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list 
    to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. 
    The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 
    
    Average: O(n ^ 2)
    Best: O(n ^ 2)
    Worst: O(n ^ 2)
    Space: Constant
    Stability: Stable
    
    * When the list is already sorted (best-case), the complexity of bubble sort is only O(n).
    * However, not only does insertion sort share this advantage, but it also performs better 
    on a list that is substantially sorted (having a small number of inversions).
    """

    def bubble_sort(self):
        """ Method to sort an array using Bubble Sort algorithm """
        # Data
        arr = self.arr
        n = self.n

        # Traverse through all array elements
        for i in range(n):
            # Last i elements are sorted
            for j in range(n - i - 1):  # At each iteration one valid element is pushed to end of the sorted list
                # Swap if current element is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


    """
    Selection sort is an in-place comparison sort.
    
    * The algorithm finds the minimum value, swaps it with the 
    value in the first position, and repeats these steps for 
    the remainder of the list. 
    
    Average: O(n ^ 2)
    Best: O(n ^ 2)
    Worst: O(n ^ 2)
    Space: Constant
    Stability: Stable
    
    * Even a perfectly sorted input requires scanning the entire array
    
    * It has O(n2) complexity, making it inefficient on large lists, 
    and generally performs worse than the similar insertion sort. 
    
    * It does no more than n swaps, and thus is useful where swapping is very expensive.
    """

    def selection_sort(self):
        """ Method to sort an array using Selection Sort algorithm """
        arr = self.arr
        n = self.n

        # Traverse through all array elements
        for i in range(n):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i

            for j in range(i + 1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr


    """
    Insertion sort is a simple sorting algorithm that is relatively efficient 
    for small lists and mostly sorted lists, and is often used as part of more 
    sophisticated algorithms. 
    
    * It works by taking elements from the list one by one and inserting them in 
    their correct position into a new sorted list.
    
    Average: O(n ^ 2)
    Best: O(n)
    Worst: O(n ^ 2)
    Space: Constant
    Stability: Stable
    
    * In the best case (already sorted), every insert requires constant time
    
    * Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(nk) 
    when each element in the input is no more than k places away from its sorted position
    
    * In arrays, the new list and the remaining elements can share the array's space, 
    but insertion is expensive, requiring shifting all following elements over by one. 
    """

    def insertion_sort(self):
        """ Method to sort an array using Insertion Sort algorithm """
        arr = self.arr
        n = self.n

        # Traverse through 1 to len(arr)
        for i in range(1, n):
            key = arr[i]  # The next item we are going to insert into the sorted section of the array

            j = i - 1  # The last item we are going to compare to

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            while j >= 0 and key < arr[j]: # If j == 0 means that this key belongs at the start
                arr[j + 1] = arr[j]  # Move the last object compared one step ahead to make room for key
                j -= 1  # Observe the next item for next time.

            # arr[j] is not greater than key means key belongs at j+1
            arr[j + 1] = key
        
        return arr

    
    """
    Average: O(n*log(n))
    Best: O(n*log(n))
    Worst: O(n*log(n))
    Space: Depends on the implementation
    Stability: Stable
    
    * On arrays, merge sort requires O(n) space; on linked lists, merge sort requires constant space.
    * In the worst case, merge sort does about 39% fewer comparisons than quicksort does in the average case.
    
    """

    def merge_sort(self):
        left = self.left
        right = self.right
        arr = self.arr
        return self.merge_sort_helper(arr, left, right)

    def merge_sort_helper(self, arr, left, right):
        """ Method to sort an array using Merge Sort algorithm """
        if left < right:
            # Same as (l+r)/2, but avoids overflow for
            # large left and right
            mid = left + (right - left) // 2

            # Sort first and second halves
            self.merge_sort_helper(arr, left, mid)
            self.merge_sort_helper(arr, mid + 1, right)

            return self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        # Merges two subarrays of arr[].
        # First subarray is arr[left..mid]
        # Second subarray is arr[mid+1..right]

        left_arr = arr[left: mid + 1]
        right_arr = arr[mid + 1: right + 1]
        i, j = 0, 0

        # Merge the temp arrays back into arr[left..right]
        for k in range(left, right + 1):
            if j >= len(right_arr) or (i < len(left_arr) and left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
        
        return arr


    """
    Average: O(n*log(n))
    Best: O(n*log(n))
    Worst: O(n ^ 2)
    Space: Constant
    Stability: Stable
    
    * Randomly picking a pivot value (or shuffling the array prior to sorting) 
    can help avoid worst case scenarios such as a perfectly sorted array.
    
    """

    def quick_sort(self):
        """ Method to sort an array using Quick Sort algorithm """
        
        left = self.left
        right = self.right
        arr = self.arr
        return self.merge_sort_helper(arr, left, right)


    def quick_sort_helper(self, arr, left, right):
        if left < right:
            # pidx is partitioning index, arr[pidx] is now
            # at right place
            pidx = self.partition(arr, left, right)

            # Separately sort elements before
            # partition and after partition
            self.quick_sort_helper(arr, left, pidx)
            self.quick_sort_helper(arr, pidx + 1, right)


    def partition(self, arr, left, right):
        # This Method takes last element as pivot, places
        # the pivot element at its correct position in sorted
        # array, and places all smaller (smaller than pivot)
        # to left of pivot and all greater elements to right
        # of pivot

        i = left - 1  # index of smaller element
        pivot = arr[right]  # pivot

        for j in range(left, right):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        
        return i + 1


    """
    Heapsort is a much more efficient version of selection sort. 
    
    *  It also works by determining the largest (or smallest) element of the list, 
    placing that at the end (or beginning) of the list, then continuing with 
    the rest of the list, but accomplishes this task efficiently by using a data structure 
    called a heap, a special type of binary tree.
        
    Average: O(n*log(n))
    Best: O(n*log(n))
    Worst: O(n*log(n))
    Space: By using input array as storage for the heap, it is possible to achieve constant space.
    Stability: Instable
    
    Once the data list has been made into a heap, the root node is guaranteed to be the 
    largest (or smallest) element. When it is removed and placed at the end of the list, 
    the heap is rearranged so the largest element remaining moves to the root. Using the heap, 
    finding the next largest element takes O(log n) time, instead of O(n) for a linear scan 
    as in simple selection sort. 
    
    This allows Heapsort to run in O(n log n) time, and this is also the worst case complexity.
    """


    def heap_sort(self):
        #  Time Complexity of Solution:
        #  Best O(nlog(n)); Average O(nlog(n)); Worst O(nlog(n)).

        #  Approach:
        #  Heap sort happens in two phases. In the first phase, the array
        #  is transformed into a heap. A heap is a binary tree where
        #  1) each node is greater than each of its children
        #  2) the tree is perfectly balanced
        #  3) all leaves are in the leftmost position available.
        #  In phase two the heap is continuously reduced to a sorted array:
        #  1) while the heap is not empty
        #  - remove the top of the head into an array
        #  - fix the heap.


        #  Technical Details:
        #  A heap is based on an array just as a hashmap is based on an
        #  array. For a heap, the children of an element n are at index
        #  2n+1 for the left child and 2n+2 for the right child.

        arr = self.arr
        length = self.right

        # convert array  to heap
        least_parent = length // 2
        for i in range(least_parent, -1, -1):
            self.move_down(arr, i, length)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if arr[0] > arr[i]:
                arr[0], arr[i] = arr[i], arr[0]
                self.move_down(arr, 0, i - 1)

        return arr

    def move_down(self, arr, first, last):
        #  The move_down method checks and verifies that the structure is a heap.
        #  The movedown function checks that an element is greater than its
        #  children. If not the values of element and child are swapped. The
        #  function continues to check and swap until the element is at a
        #  position where it is greater than its children.

        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            if (largest < last) and (arr[largest] < arr[largest + 1]):
                largest += 1

            # right child is larger than parent
            if arr[largest] > arr[first]:
                arr[largest], arr[first] = arr[first], arr[largest]
                # move down to largest child
                first = largest
                largest = 2 * first + 1
            else:
                return  # force exit


if __name__ == '__main__'
  arr = [random.randint(-10, 10) for i in range(10)]
  sort = Sort(arr)
  print(sort.merge_sort())
  print(sort.quick_sort())
  print(sort.heap_sort())
  print(sort.selection_sort())
  print(sort.bubble_sort())
  print(sort.insertion_sort())
