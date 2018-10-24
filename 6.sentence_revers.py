'''
str = input("Enter A sentence :")
print (' '.join(str.split()[::-1]))
'''

def reverse(string) :
    string = string.strip()
    result = [word[::-1] for word in string[::-1].split(" ")]
    revers = " ".join(result)
    print("The reverse sentence is :",revers)



string = input("Enter A sentence :")
print("The sentence is : ", string)
reverse(string)
