Concept:

    •	Two pointers involve having a left (L) pointer and a right (R) pointer, both starting at some indices of an array.
    •	L and R pointers do not have to start at the beginning of the array, unlike in the sliding window technique.
    •	The pointers are usually moved based on conditions in the problem, until they meet.

General Steps:

    1.	Initialize L at index 0 and R at index arr.length - 1.
    2.	Move L and R depending on the problem conditions.
    3.	Continue until L meets R.

Example 1: Palindrome Check

    •	Problem: Check if a word is a palindrome (reads the same forwards and backwards).
    •	Approach:
    •	Start L at 0 and R at the last index of the word.
    •	Compare the characters at L and R.
    •	If they don’t match, return False. If they match, move L and R inward until they meet.

```python
def isPalindrome(word):
L, R = 0, len(word) - 1
while L < R:
if word[L] != word[R]:
return False
L += 1
R -= 1
return True
```

    •	Time Complexity: O(n), where n is the length of the input word. Each character is visited once.

Example 2: Target Sum in a Sorted Array

    •	Problem: Given a sorted array, find two indices of elements that sum up to a target value. Assume one solution exists.
    •	Approach:
    •	Use two pointers (L at the start, R at the end).
    •	Calculate the sum of elements at L and R.
    •	If the sum is greater than the target, decrement R to reduce the sum.
    •	If the sum is smaller than the target, increment L to increase the sum.
    •	If the sum matches the target, return the indices [L, R].

def targetSum(nums, target):
L, R = 0, len(nums) - 1
while L < R:
if nums[L] + nums[R] > target:
R -= 1
elif nums[L] + nums[R] < target:
L += 1
else:
return [L, R]

    •	Time Complexity: O(n), where n is the length of the input array. Each element is visited once.

Summary:

    •	Two pointers can reduce time complexity compared to brute force methods.
    •	Time Complexity: O(n) in both examples, as each element or character is visited once.
