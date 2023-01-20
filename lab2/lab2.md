# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
    # use recursion to calculate the same result
    if number > 0:
        return number * number + function1(number - 1)
    else:
        return 0
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
    # use recursion to calculate the same result
    if number == 0:
        return 0
    return number * number + function2(number - 1)

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
    # use recursion and the bubble sort algorithm to sort the list
    if len(list) == 1:
        return list
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
    return function3(list[:-1]) + [list[-1]]

```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
    # use recursion to calculate the same result
    if number == 1:
        return 1
    return number * function4(number - 1)
```


## In class portion


### Group members
List the members of your group member below:

	* Name 
	* ex. Samuel Vimes
	* ...

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Darshan pandya |  4.7918 | 1.00775 |

### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number | 4.2259 | 4.9157 | 0.6898 |
|fibonacci | 0.9876 | 1.0174 | 0.0298 |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.


## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?

Answer: The fastest version of code is the recursive version, and the slowest version of code is the iterative version.

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)? 

Answer: The recursive version uses more space than the iterative version.

3. What sort of conclusions can you draw based on your observations?

Answer: The recursive version is more efficient than the iterative version.



