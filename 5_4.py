# the_calls.txt
# calls.txt

list_A = []
list_B = []
with open('the_calls.txt','r') as tc:
    with open('calls.txt','w') as call:
        for line in tc:
            current_list = line.replace('\n','').split('\t')
            if (current_list[2] == 'A'):
                list_A.append(current_list)
                list_A[-1][1] = int(list_A[-1][1])
            else:
                list_B.append(current_list)
                list_B[-1][1] = int(list_B[-1][1])
        list_A.sort(key = lambda x: x[1], reverse = True)
        list_B.sort(key = lambda x: x[1], reverse = True)
        for list in list_A:
            for item in list:
                print(item,end = '\t', file = call)
            print(file = call)
        for list in list_B:
            for item in list:
                print(item,end = '\t', file = call)
            print(file = call)