'''
simple input = shihab khan dhaka bangladesh
simple output =
s:2
h:5
i:1
a:6
b:2
k:2
n:2
d:2
g:1
l:1
e:1

'''

string = input("Enter a String :")
i = 0
temp_var = " "
while i < len(string):
    if string[i] not in temp_var:
        temp_var += string[i]
        print(f"{string[i]}:{string.count(string[i])}")
    i += 1
