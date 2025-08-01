# 1201. Ugly Number III neetcode

## Code

```python
import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:


        def countUglyNumbers(x):
            ab = math.lcm(a,b)
            ac = math.lcm(a,c)
            bc = math.lcm(b,c)
            abc = math.lcm(a,b,c)
            return (x//a) + (x//b) + (x//c) - (x//ab) - (x//ac) - (x//bc) + (x//abc)
        
        low = 1
        high = 2 * 10**9

        while low < high:
            mid = (low + high) // 2
            if countUglyNumbers(mid) < n:
                low = mid + 1
            else:
                high = mid
        return low
```

## Logic

- Step 1: 


