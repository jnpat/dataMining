import random

itemSize = 50
item = []
minSup = 2
answer = []
check = 0
once = False

for i in range(itemSize):
    item.append("Item" + str(i+1))

def random1():
    transList = []
    a = []
    tranSize = 1000
    p = 8

    for i in range(tranSize):
        if i<p:
            a.append(("T" + str(i),random.randint(2,5)))
        else:
            a.append(("T" + str(i),random.randint(6,8)))

        transList.append(("T" + str(i) ,random.sample(item, a[i][1])))
    
    print1(transList)
    return transList

def findSup(list1):
    countTran = [0]*len(list1)
    listItem = []
    itemname = []
    sup = 0

    for i in range(len(item)):
        for j in range(len(list1)):
            for k in range(len(list1[j][1])):
                if item[i] == list1[j][1][k]:
                    countTran[j] = 1
                    sup += 1
        itemname.append("Item" + str(i+1))
        listItem.append((itemname,countTran,float(sup)/len(list1)*100,1))
        itemname = []
        countTran = [0]*len(list1)
        sup = 0

    print1(listItem)
    return listItem
    
def findFreqItem(list1):
    freqItem = []
    
    for i in range(len(list1)):
        if list1[i][2] >= minSup:
            answer.append(list1[i])
            freqItem.append(list1[i])
            
    if len(freqItem) == 0:
        print("no item support more than minsup")
        return freqItem
        
    print1(freqItem)
    
    return freqItem


def matching(list1):
    if len(list1) == 0: return answer
    listmatch = [0]*len(list1[0][1])
    itemSet = []
    listreturn = []
    sup = 0
    keepsup = 0 
    for i in range(len(list1)):
        j = i+1
        while(j<len(list1)):
            for k in range(len(list1[i][1])):
                if list1[i][1][k] == list1[j][1][k] and list1[i][1][k] == 1:
                    listmatch[k] = 1
                    sup += 1
                    if len(list1[i][0]) and len(list1[j][0]) == 1:
                        itemSet = list1[i][0] + list1[j][0]
                        keepsup = list1[i][2]
                    else:
                        for l in range(len(list1[i][0])):
                            for m in range(len(list1[j][0])):
                              if list1[i][0][l] == list1[j][0][m]:
                                keepsup = list1[i][2]
                                itemSet = list1[i][0]+list1[j][0]
                                listduplicate(itemSet)
                                
            if len(itemSet) > 0:
                listreturn.append((itemSet,listmatch,float(sup)/len(list1[i][1])*100,keepsup))
            itemSet = []
            sup = 0
            j=j+1
            listmatch = [0]*len(list1[0][1])
    print1(listreturn)

    while len(listreturn) > 1:
        return matching(findFreqItem(listreturn))
    if len(listreturn) == 1: 
        return listreturn
    else:
        return 1
    
def listduplicate(list1):
    for i in range(len(list1)):
        j=i+1
        while j<len(list1):
            if list1[i]==list1[j]:
                list1.remove(list1[i])
            j += 1
                
    return list1

def print1(list1):
    f = open("result1.txt","a")
    # print(len(list1))
    if len(list1[0]) ==2:
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for i in range(len(list1)):
            f.write(str(list1[i]) + "\n")
    else:
        f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for j in range(len(list1)):
            f.write("Item Set = " + str(list1[j][0]) +  " Transaction = " + str(len(list1[j][1]))
            + " Support = " + str(list1[j][2]) + " SupportPair = " + str(list1[j][3]) + "\n")
    f.close()  


# main
ans = random1()
ans = findSup(ans)
ans = findFreqItem(ans)
ans = matching(ans)
# print("ans is")
# # print(ans)
# print("-------------------------------------------")

f = open("result.txt","w+")

for i in range(len(answer)):
    if len(answer[i][0])==1:
        f.write("Item Set = " + str(answer[i][0]) + "       Support = " + str(answer[i][2])+ "        Size = " + str(len(answer[i][0])) +"\n")
    else:
        f.write("Item Set = " + str(answer[i][0]) + "       Support = " + str(answer[i][2])+ "        Size = " + str(len(answer[i][0])) + "       conf = "+str(answer[i][2]/answer[i][3]*100) + "\n")

f.close()