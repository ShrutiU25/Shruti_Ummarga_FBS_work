#Q8. Print 1 to 100 in snakes and ladder pattern.

li = []
for i in range(9, -1, -1):
    sub_li = []
    for j in range(i * 10 + 1, (i * 10 + 1) + 10): #((i + 1) * 10 + 1)
        #print(j, end = ' ')

        #sub_li.append(j)
        sub_li = sub_li + [j]

    #li.append(sub_li)
    if(i % 2 != 0):
        sub_li.reverse()

    li = li + [sub_li]

#print(li)
#########################################
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j], end = ' ')
    print()                