# copy over your code from lab 1 to this file

def fibonacci(n):
    '''
    Returns the nth fibonacci number where the first two numbers are 0 and 1

    Parameters:
        n (int): the index of the fibonacci number to return

    Returns:
        int: the nth fibonacci number 
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sum_to_goal(numbers, goal):
    '''
    Returns the product of the two numbers in the list that sum to the goal

    Parameters:
        numbers (list): list of numbers to search
        goal (int): the goal sum

    Returns:
        int: the product of the two numbers that sum to the goal
    '''
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0



