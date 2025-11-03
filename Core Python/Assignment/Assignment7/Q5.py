#    1 
#   1 2 
#  1   3
# 1     4
#1 2 3 4 5

for i in range(1,6):
    print(' ' * (5 - i), end = ' ')
    for j in range(1, i + 1):
        if(j == 1 or j == i or i == 5):
            print(j, end = ' ')
        else:
            print(' ', end = ' ')
    print()
