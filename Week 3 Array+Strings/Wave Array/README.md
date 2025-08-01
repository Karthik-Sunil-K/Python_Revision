# Wave Array

## Code
```text
Wave Array
Difficulty: MediumAccuracy: 63.69%Submissions: 274K+Points: 4Average Time: 20m
Given an sorted array arr[] of integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5] ..... and so on. If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and modify the given array in-place without returning a new array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.
Input: arr[] = [2, 4, 7, 8, 9, 10]
Output: [4, 2, 8, 7, 10, 9]
Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.
Input: arr[] = [1]
Output: [1]
Constraints:
1 ≤ arr.size ≤ 106
0 ≤ arr[i] ≤109

```


```python
class Solution:
    def sortInWave(self, arr):
        
        left = 0
        right = 1
        n = len(arr)
        
        while right < n:
            arr[left], arr[right] = arr[right], arr[left]
            left += 2
            right += 2
```

## Logic

- Take 2 pointers and assing the values as 0 and 1 (first 2 values)
- Swap the numbers you can use a temp variable if needed otherwise swap with a,b=b,a syntax
- Increment both the pointers by 2 till the second point end 

