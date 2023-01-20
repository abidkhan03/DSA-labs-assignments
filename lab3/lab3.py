#
# Author: Darshan pandya
# Student Number: 120846217
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#


def factorial(number):
	'''
	Returns the factorial of the number

	Parameters:
		number (int): the number to find the factorial of the number

	Returns:
		int: the factorial of the number
	'''
	if number == 0:
		return 1
	return number * factorial(number - 1)



def linear_search(list, key):
	'''
	Returns the index of the key in the list if it exists and -1 otherwise

	Parameters:
		list (list): the list to search
		key (int): the key to search for

	Returns:
		int: the index of the key in the list if it exists, -1 otherwise
	'''

	if len(list) == 0:
		return -1
	if list[0] == key:
		return 0
	# recursive call on the rest of the list
	index = linear_search(list[1:], key)
	if index == -1:
		return -1
	# add 1 to the index returned by the recursive call
	return index + 1

	
	
def binary_search(list, key):
	'''
	Returns the index of the key in the list if it exists and -1 otherwise

	Parameters:
		list (list): the list to search
		key (int): the key to search for

	Returns:
		int: the index of the key in the list if it exists, -1 otherwise
	'''

	if len(list) == 0:
		return -1
	# mid is the index of the middle element
	mid = len(list) // 2
	if list[mid] == key:
		return mid
	elif list[mid] > key:
		# recursive call on the left half of the list
		return binary_search(list[:mid], key)
	else:
		# recursive call on the right half of the list
		index = binary_search(list[mid+1:], key)
		if index == -1:
			return -1
		# add mid + 1 to the index returned by the recursive call
		return index + mid + 1

