## Prefix Sums

    Prefix Sum is a technique for working with arrays.

    We create a new array (called prefix) where each element at index i is the sum of the original array (nums) from the start (index 0) up to i.

    For example, if nums = [2, -1, 3, -3, 4], the prefix sum array will be [2, 1, 4, 1, 5].

## Example: Range Sum Query

    The task is to create a structure that can quickly calculate the sum of any part (subarray) of the array.

    To do this, we can use a PrefixSum class, which will:

    1.	Take the array nums as input.

    2.	Create a prefix sum by adding each element to a running total and storing it in a prefix array.

```python
class PrefixSum:
    def __init__(self, nums):
      self.prefix = []
      total = 0
      for n in nums:
         total += n
         self.prefix.append(total)
```

## Fast Query for Subarray Sum

    Once we have the prefix sum, we can quickly calculate the sum of any subarray between indices left and right in constant time O(1).

    Formula: prefix[right] - prefix[left - 1].

    This subtracts the sum before the left index from the sum at the right index.

    If left is 0, there’s no need to subtract (we handle this to avoid errors).

## Range Sum Function:

```python
   def rangeSum(self, left, right):
       preRight = self.prefix[right]
       preLeft = self.prefix[left - 1] if left > 0 else 0

       return (preRight - preLeft)
```

## Time and Space Complexity

    Building the prefix sum takes O(n) time (where n is the length of the array).

    Querying the sum of a subarray takes O(1) time (constant time, no matter the size of the array).

    Space complexity is O(n) unless we overwrite the original array with the prefix sum, which can reduce it to O(1).

## Let's See How Prefix Sum Calculated??

/// image

## Additional Notes

    Prefix sums can also be used for other operations like calculating products.

    A postfix sum is the reverse: it starts from the end of the array and calculates the sum backwards.
