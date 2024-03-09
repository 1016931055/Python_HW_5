# med_research.txt.txt
# output.txt

row = 0
column = 0
matrix = []
with open('med_research.txt','r') as res:
    with open('output.txt','w') as out:
        for line in res:
            matrix.append(list(line.split()))
            row += 1  #行数
        column = len(matrix[0])  #列数

        for i in range(column):
            for j in range(row):
                print(matrix[j][i],end = ' ',file = out)
            print(file = out)
    out.close()
res.close()