"""
    Write a program that accepts user input to create a list of integers. 
    Then, compute the sum of all the integers in the list.
"""


def sum_items():
    items = input("Enter a list of integrs separated by space: ")
    my_list = items.split()

    integers = [int(num) for num in my_list if num.isdigit()]

    total = sum(integers)
    print("The total sum of the ", total)


sum_items()
