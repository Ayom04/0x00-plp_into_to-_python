user_information = {
    "name": "John",
    "age": 30,
    "favourite_colour": "red",
}

name = input("Please enter your name: ")
age = input("Please enter your age: ")
favourite_colour = input("Please enter your favourite colour: ")

user_information["name"] = name
user_information["age"] = age
user_information["favourite_colour"] = favourite_colour


print("here is your detail", user_information)
