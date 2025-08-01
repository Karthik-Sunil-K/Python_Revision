# Equilibrium Point

## Code
```text
Equilibrium Point
Difficulty: EasyAccuracy: 28.13%Submissions: 652K+Points: 2Average Time: 15m
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.

```


```python
class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        left_sum = 0
        tot_sum = sum(arr)

        for i in range(len(arr)):
            if left_sum == (tot_sum - left_sum - arr[i]):
                return i
            left_sum+=arr[i]
        return -1
```

## Logic

- The total sum is left_side_sum + right_side_sum + arr[i]
- check left_sum == right_sum
- that is left_sum = tot_sum - left_sum - arr[i] 
- if both are equal return its index that is i
- 

