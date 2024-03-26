"""
    Write a program that accepts user input to create two sets of integers.
    Then, create a new set that contains only the elements that are common to both sets.
"""
first = input("Please enter a set of numbers separated with space: ")
second = input("Please enter another set of numbers separated with space: ")

first = set(first.split())
second = set(second.split())
print(first & second)
