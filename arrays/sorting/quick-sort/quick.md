Here’s the content in markdown format:

# Quick Sort

QuickSort is a sorting algorithm based on the Divide and Conquer principle. It picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

## How does QuickSort Algorithm work?

There are mainly three steps in the algorithm:

1. we choose a pivot point
2. Start with 2 indices i and j and a temp variable (for swapping purpose)
   ![initials](/public/quick-sort/8.png)
3. check if our pivot value is greater than or smaller to pivot,
   - if greater, then increment j, and leave i as it is.
   - if smaller, then increment i and swap the values of i and j using temp variable.
   ![initials-2](/public/quick-sort/9.png)
4. Repeat the steps until j reached the pivot point.

  This is how our array will going to look like after 1 partition.
  - all the elements less than the pivot will be on the left side and all the elements greater than the pivot will be on the right side.
  - ![initials-3](/public/quick-sort/10.png)

5. Now we will do the same for the left and right side of the pivot.
  - ![initials-4](/public/quick-sort/11.png)


## Choice of Pivot:

There are many different choices for picking pivots:

- **Always pick the first (or last) element as the pivot:** The below implementation picks the last element as pivot. The problem with this approach is that it results in the worst case when the array is already sorted.
- **Pick a random element as the pivot:** This is a preferred approach because it does not have a pattern for which the worst case happens.
- **Pick the median element as the pivot:** This is ideal in terms of time complexity as we can find the median in linear time. The partition function will always divide the input array into two halves. However, it is slower on average because median finding has high constants.

## Partition Algorithm:

The key process in QuickSort is `partition()`. There are three common algorithms to partition. All these algorithms have O(n) time complexity.

1. **Naive Partition:**
   In this method, we create a copy of the array. First, we put all smaller elements, then all greater ones. Finally, we copy the temporary array back to the original array. This requires O(n) extra space.

2. **Lomuto Partition:**
   This is the partition method used in this article. It’s a simple algorithm where we keep track of the index of smaller elements and keep swapping them. It's used here because of its simplicity.

3. **Hoare’s Partition:**
   This is the fastest method. Here, we traverse the array from both sides and keep swapping greater elements on the left with smaller elements on the right until the array is partitioned. Please refer to [Hoare’s vs Lomuto](#) for details.

Let me know if you'd like to add or adjust anything!

![Quick sort](/public/quick-sort/QuickSort2.png)

---

## Details of the Partition Algorithm and Illustration:

The logic is simple: we start from the leftmost element and keep track of the index of smaller (or equal) elements as `i`. While traversing, if we find a smaller element, we swap the current element with `arr[i]`. Otherwise, we ignore the current element.

Let us understand the working of partition and the Quick Sort algorithm with the help of the following example:

Consider: `arr[] = {10, 80, 30, 90, 40}`

- **Step 1:** Compare 10 with the pivot, and since it is less than the pivot, arrange it accordingly.
  ![Partition in QuickSort: Compare pivot with 10](/public/quick-sort/1.webp)

- **Step 2:** Compare 80 with the pivot. It is greater than the pivot, so we do nothing.
  ![Partition in QuickSort: Compare pivot with 80](/public/quick-sort/2.webp)

- **Step 3:** Compare 30 with the pivot. It is less than the pivot, so arrange it accordingly.
  ![Partition in QuickSort: Compare pivot with 30](/public/quick-sort/3.webp)

- **Step 4:** Compare 90 with the pivot. It is greater than the pivot, so we do nothing.
  ![Partition in QuickSort: Compare pivot with 90](/public/quick-sort/4.webp)

- **Step 5:** Finally, arrange the pivot in its correct position.
  ![Partition in QuickSort: Place pivot in its correct position](/public/quick-sort/5.webp)

## Illustration of QuickSort Algorithm:
The partition keeps placing the pivot in its actual position in the sorted array. Repeatedly placing pivots in their correct positions makes the array sorted.

Follow the below images to understand how the recursive implementation of the partition algorithm helps to sort the array:

- **Initial partition on the main array:**
  ![Quicksort: Performing the partition](/public/quick-sort/6.webp)

- **Partitioning of the subarrays:**
  ![Quicksort: Performing the partition](/public/quick-sort/7.webp)

Quick Sort is a crucial algorithm in the industry, but there are other sorting algorithms that may be more optimal in different cases. To gain a deeper understanding of sorting and other essential algorithms, check out our course *Tech Interview 101 – From DSA to System Design*. This course covers almost every standard algorithm and more.

---

### Time Complexity:

- **Best Case:**
  Ω(N log(N))
  The best-case scenario for Quicksort occurs when the pivot chosen at each step divides the array into roughly equal halves. In this case, the algorithm will make balanced partitions, leading to efficient sorting.

- **Average Case:**
  θ(N log(N))
  Quicksort’s average-case performance is usually very good in practice, making it one of the fastest sorting algorithms.

- **Worst Case:**
  O(N²)
  The worst-case scenario for Quicksort occurs when the pivot at each step consistently results in highly unbalanced partitions, such as when the array is already sorted and the pivot is always chosen as the smallest or largest element. To mitigate the worst-case scenario, various techniques are used, such as choosing a good pivot (e.g., median of three) and using a randomized algorithm (Randomized Quicksort) to shuffle the elements before sorting.

### Auxiliary Space:

- **O(1)** (if we don’t consider the recursive stack space).
  If we consider the recursive stack space, then, in the worst case, Quicksort could make O(N) space.

---

## Advantages of Quick Sort:

- It is a **divide-and-conquer algorithm** that makes it easier to solve problems.
- It is **efficient on large data sets**.
- It has a **low overhead**, requiring only a small amount of memory to function.
- It is **cache-friendly** as it works on the same array to sort and does not copy data to any auxiliary array.
- It is the **fastest general-purpose algorithm** for large data when stability is not required.
- It is **tail recursive**, allowing for tail call optimizations.

---

## Disadvantages of Quick Sort:

- It has a **worst-case time complexity** of O(N²), which occurs when the pivot is chosen poorly.
- It is **not a good choice for small data sets**.
- It is **not a stable sort**, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output. This is because Quicksort swaps elements according to the pivot’s position, without considering their original positions.
