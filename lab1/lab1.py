# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: 
# Student Number:120846217
# Student Name : Darshan pandya 


def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower()
    if player == opponent:
        return False
    if player == 'rock':
        if opponent == 'scissors':
            return True
        else:
            return False
    if player == 'paper':
        if opponent == 'rock':
            return True
        else:
            return False
    if player == 'scissors':
        if opponent == 'paper':
            return True
        else:
            return False


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0
    

class UpCounter:
    def __init__(self, step_size=1):
        self.count_value = 0
        self.step_size = step_size

    def count(self):
        return self.count_value

    def update(self):
        self.count_value += self.step_size



class DownCounter(UpCounter):
    def update(self):
        self.count_value -= self.step_size



