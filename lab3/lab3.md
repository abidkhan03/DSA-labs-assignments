# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```

##### Analyzed function 1

```python
def function1(value, number):
	'''
	Returns the value raised to the power of number

	Parameters:
		value (int): the value to raise to the power of number
		number (int): the power to raise the value to

	Returns:
		int: the value raised to the power of number
	'''
	return 1 if number == 0 else value * function1(value, number - 1) \
			if number == 1 else value * function1(value, number - 1)
```

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```

##### Analyzed function 2

```python
def function2(mystring):
	'''
	Returns True if the string is a palindrome and False otherwise

	Parameters:
		mystring (str): the string to check if it is a palindrome

	Returns:
		bool: True if the string is a palindrome and False otherwise
	'''
	return recursive_function2(mystring, 0, len(mystring) - 1)

def recursive_function2(mystring, a, b):
	'''
	Returns True if the string is a palindrome and False otherwise

	Parameters:
		mystring (str): the string to check if it is a palindrome
		a (int): the starting index of the string
		b (int): the ending index of the string

	Returns:
		bool: True if the string is a palindrome and False otherwise
	'''
	return True if a >= b else False if mystring[a] != mystring[b] else \
			recursive_function2(mystring, a + 1, b - 1)
```

### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```

##### Analyzed function 3

```python
def function3(value, number):
	'''
	Returns the value raised to the power of number

	Parameters:
		value (int): the value to raise to the power of number
		number (int): the power to raise the value to

	Returns:
		int: the value raised to the power of number
	'''
	return 1 if number == 0 else value * function3(value, number - 1) \
			if number == 1 else function3(value, number // 2) ** 2 \
			if number % 2 == 0 else value * function3(value, number // 2) ** 2
```

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?

Answer: The first step is to identify the base case. The base case is the case where the function returns a value without 
making any recursive calls. The second step is to identify the recursive case. The recursive case is the case where the 
function calls itself. The third step is to write down the recursive relation. The recursive relation is the relation 
between the function and its recursive calls. The fourth step is to write down the function. The fifth step is to test 
the function.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 

Answer: The process of analyzing recursive functions is similar to the process of analyzing non-recursive functions. 
The difference is that the recursive functions have recursive calls. The recursive calls are analyzed in the same way 
as the non-recursive functions. The recursive calls are analyzed by counting the number of times the function is called.
The recursive calls are also analyzed by counting the number of times the function is called for each input size.

