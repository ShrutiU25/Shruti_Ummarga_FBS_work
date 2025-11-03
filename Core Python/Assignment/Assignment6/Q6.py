#      1 
#    1 2 3 
#   1 2 3 4 5
#  1 2 3 4 5 6 7
#1 2 3 4 5 6 7 8 9


for i in range(1,6):
    print(' ' * (5 - i), end = ' ')  
    for j in range(1, 2 * i):
        print(j, end = ' ')
    print()
