
def reverse_string(string):
    reversed_string = ""
    for i in string:
        reversed_string = i+reversed_string
    print("Revers of the string is :", reversed_string)


string = input("Enter a string :")
print("The string is :", string)
reverse_string(string)
