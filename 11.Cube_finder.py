'''
input :Enter Last range of Number :10
output :{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}


'''
def cube_finder(number):
    cubes = {}
    for i in range(1,number+1):
        cubes[i]=i**3
    print(cubes)

n = int(input("Enter Last range of Number :"))
print(cube_finder(n))
