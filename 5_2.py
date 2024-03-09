# poe_unpublished.txt
# poe_decode_attempt.txt

list1 = []
with open('poe_unpublished.txt','r') as pun:
    with open('poe_decode_attempt.txt','w') as pda:
        for line in pun:
            list1.append(line.split())
            list1[-1].sort(key = len)
        list1.sort(key = len)

        for i in range(len(list1)):
            for j in range(len(list1[i])):
                print(list1[i][j],end=" ",file = pda)
            print(file = pda)
    pda.close()
pun.close()
