"""
    Create a program that stores a list of words. Then, 
    use list comprehension to create a new list that 
    contains only the words that have an odd number of characters.
"""


def odd_words():
    words = input("Enter a list of words separated by space: ")
    my_list = words.split()

    odd_words = [word for word in my_list if len(word) % 2 != 0]

    print(odd_words)


odd_words()
