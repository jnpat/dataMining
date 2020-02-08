import random

itemSize = 10
item = []

for i in range(itemSize):
    item.append("Item" + str(i+1))

def random1():
    transList = []
    a = []
    tranSize = 10
    p = 8

    for i in range(tranSize):
        if i<p:
            a.append(("T" + str(i),random.randint(2,5)))
        else:
            a.append(("T" + str(i),random.randint(6,8)))

        transList.append(("T" + str(i) ,random.sample(item, a[i][1])))

    print(str(transList) + "\n")   
    return transList

def association(list1):
    countTran = []
    a = []
    for i in range(len(list1)):
        print(list1[i][1],len(list1[i][1]))
        for j in range(len(list1[i][1])):
            print(list1[i][1][j])
            for k in range(len(item)):
                if item[k] == list1[i][1][j]:
                    a.append(list1[i][0])
                countTran.append(item[k],a)
                a = []
        

            


# main
association(random1())