# two pointer

usually two pointer problem involves a slow and fast pointer. as for current experience it would be easier to do with a while loop as shown

```python
slow_ptr = 0
fast_ptr = 1

while slow_ptr < some_arbitary_length:
    if cond_1:
        slow_ptr += 1
        fast_ptr += 1
```

most of the time we would only need to traverse and compare at n time complexity, or traverse the full length once.

## two pointer common pattern

1. both pointer move together per iteration, a for loop might be clearer in terms of ending signal (remember python range counts from 0)
2. both pointer don't move together, lags between pointer movement, usually we would only need to check the fast pointer

## to identify a two pointer problem

1. traverse and comparison


## to take note

- timing to move each pointer is crucial, missed timing is undesired
- nested for loop requires additional attention on the item we are iterating (is it the actual value or the count?)
    - also nested for loop only works if we are checking all elements **to** an example