# recursion

recursion come in a few forms


to search something deep in the leaf. we will place the terminate condition on top of the recursion function such that it will only terminate at the leaf (or equivalent), else it will reassign the current node to the next node.

```python
def some_function(current_node):
    if current_node.next is None:
        print(current_node.value)
    current_node = current_node.next
    some_function(current_node)
```


to validate the entire data structure.

```python
def some_function(current_node):
    if current_node.value:
        return True
    current_node = current_node.next
    return some_function(current_node)
```

requires one to have a good stopping condition eg. linked list should we use 

```python
if current_node is None
```
or 
```python
if current_node.next is None
```
as stopping condition?

sometimes the stopping condition could be more than one.