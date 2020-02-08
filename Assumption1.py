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
    listitem = []
    listcount = [0]*len(list1)
    sup = 0
    t = []
    for i in range(len(list1)):
        t.append(i)
    # for i in range(len(list1)):
    #     # print(list1[i][1],len(list1[i][1]))
    #     for j in range(len(list1[i][1])):
    #         # print(list1[i][1][j])
    #         for k in range(len(item)):
    #             if item[k] == list1[i][1][j]:
    #                 a.append(list1[i][0])
    #                 print(a)
    #     countTran.append(item[k],a)
    #     a = []
    for i in range(len(item)):
        for j in range(len(list1)):
            for k in range(len(list1[j][1])):
                # print(len(list1[1][1]))
                if item[i] == list1[j][1][k]:
                    # print(list1[j][1][k])
                    a.append(list1[j][0])
                    listcount[j] = 1
                    sup = sup + 1
                    # print(a)
        listitem.append(("ITEM" + str(i+1) , a,listcount,sup))
        listcount = [0]*len(list1)
        a=[]
        sup = 0
    # print(listitem)  
    print("Item            transaction ID            Support")
    print("       "+str(t))
    for i in range(len(item)):
        if i < 9:
            print(str(listitem[i][0])+"  "+str(listitem[i][2])+"       "+str(listitem[i][3]/len(list1))) 
        else:
            print(str(listitem[i][0])+" "+str(listitem[i][2])+"       "+str(listitem[i][3]/len(list1))) 
        
               




# main
association(random1())

