list1 = []
list2 = []
i = 1
with open('weights.txt','r') as wts:
    with open('team.txt','w') as team:
        for line in wts:
            if(i % 2 == 1): #奇数位
                list1.append(line.split())
                list1[-1][1] = float(list1[-1][1])
            else:
                list2.append(line.split())
                list2[-1][1] = float(list2[-1][1])
            i += 1

        list1.sort(key = lambda x: x[1], reverse = True)  #对[1]降序排列
        list2.sort(key = lambda x: x[1], reverse = True)

        for j in range(len(list2)):
            print(list2[j][0],list2[j][1],file = team,sep = ' ', end='\n')
        for k in range(len(list1)):
            print(list1[k][0],list1[k][1],file = team,sep = ' ', end='\n')
    team.close()
wts.close()
