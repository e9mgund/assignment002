number_list = [i for i in range(0,101) if i % 2 == 0]

for i in range(len(number_list)) :
    print(f'{i+1}: {number_list[i]}')