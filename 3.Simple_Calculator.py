
def calculator():
    operation = input('''
Please Type operatin Would you like to complete :
+ for addition
- for subtraction  
* for multiplication 
/ for division
% for modulus
** for square

 ''')

    number_1 = int(input("Enter First Number :"))
    number_2 = int(input("Enter Second  Number :"))

    if operation == '+':
        print(f'{number_1} + {number_2} =')
        print(number_1 + number_2)

    elif operation == '-':
        print(f'{number_1} - {number_2} =')
        print(number_1 - number_2)

    elif operation == '*':
        print(f'{number_1} * {number_2} =')
        print(number_1 * number_2)

    elif operation == '/':
        print(f'{number_1} / {number_2} =')
        print(number_1 / number_2)

    elif operation == '%':
        print(f'{number_1} % {number_2} =')
        print(number_1 % number_2)

    elif operation == '**':
        print(f'{number_1} ** {number_2} =')
        print(number_1 ** number_2)
    else:
        print("You don't type valid oeration ! Please run the program again ")

    again()

def again():
    calcuate_again = input('''
    Do You Calculate Again ?
    Please Type Y for Yes N for No.
''')
    if calcuate_again.upper() == 'Y':
        calculator()
    elif calcuate_again.upper()=='N':
        print("See You leter \U0001F602 ")
    else:
        again()


calculator()












































