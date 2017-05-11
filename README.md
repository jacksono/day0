
[![Build Status](https://travis-ci.org/jacksono/day0.svg?branch=master)](https://travis-ci.org/jacksono/day0)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/642fe647d4214de89a79683da184edf7/badge.svg)](https://www.quantifiedcode.com/app/project/642fe647d4214de89a79683da184edf7)
[![Coverage Status](https://coveralls.io/repos/github/jacksono/day0/badge.svg?branch=master)](https://coveralls.io/github/jacksono/day0?branch=master)
# day0_bootcamp(taken over)
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
Since one(1) loop has a result of **O(n)** - linear time complexity, the nesting with one
loop makes the result to be **O(n2)**- quadratic time complexity

And that is the asymptotic analysis for that PRIME NUMBERS function.
