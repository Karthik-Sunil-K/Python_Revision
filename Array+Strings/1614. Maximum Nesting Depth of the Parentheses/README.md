# 1614. Maximum Nesting Depth of the Parentheses

## Code

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxx = 0
        for letter in s:
            if letter == "(":
                count+=1
                maxx=max(count,maxx)
            elif letter == ")" and count>0:
                count-=1
        return maxx
```

## Logic

- Check the opening brackets and and increment the counter
- check the closing bracket and decrease the counter  
- Each time check max of the counter since it will increment and decrement 
- Since it is a valid paranthesis the total opened will be the answer


