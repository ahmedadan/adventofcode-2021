def get_num_increases(list):
    num = 0    
    for i in range(1,len(list)):
        if list[i] > list[i-1]:
            num = num + 1
    return num        
    

# part 1
f = open("data.txt", "r")

depths = []
for l in f:
    depths.append(int(l))

print(get_num_increases(depths))

# part 2
sums = []
for i in range(2,len(depths)):
    sums.append(depths[i] + depths[i-1] + depths[i-2])

print(get_num_increases(sums))  