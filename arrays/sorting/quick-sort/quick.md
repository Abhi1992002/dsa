Here’s the content in markdown format:

```markdown
# Quick Sort

**Last Updated** : 01 Sep, 2024

QuickSort is a sorting algorithm based on the Divide and Conquer principle. It picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

## How does QuickSort Algorithm work?

There are mainly three steps in the algorithm:

1. **Choose a pivot.**
2. **Partition the array** around the pivot. After partition, it is ensured that all elements on the left of the pivot are smaller, and all elements on the right are greater. The left and right subarrays may not be sorted individually.
3. **Recursively call QuickSort** for the two partitioned left and right subarrays.
4. **Stop recursion** when there is only one element left.

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
```

Let me know if you'd like to add or adjust anything!

![Quick sort](public/QuickSort2.png)
