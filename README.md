# day0
bootcamp week1 day 0 python exercise

#Asymptotic analysis of the function prime_numbers()
The function contains a nested loop as below
```python
for i in range(n + 1):
        is_prime = True
        divisor = 2
        while divisor < i:
            if i % divisor == 0:
                is_prime = False
                divisor += 1
```
Since one loop has a result of **O(n)** - linear time complexity, the nesting with one
loop makes the result to be **O(n2)**- quadratic time complexity

And that is the asymptotic analysis for that function
