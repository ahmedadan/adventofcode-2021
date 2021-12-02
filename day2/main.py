f = open("data.txt", "r")

direction = []
value = []

position = 0
depth = 0

for l in f:
    direction.append(l.split(" ")[0])
    value.append(l.split(" ")[1])

for i in range(direction.__len__()):
    if direction[i] == "forward":
        position += int(value[i])
    elif direction[i] == "up":
        depth -= int(value[i])
    elif direction[i] == "down":
        depth += int(value[i])

f.close()

print("Part 1: " + str(position*depth))

f = open("data.txt", "r")

direction = []
value = []

position = 0
depth = 0
aim = 0

for l in f:
    direction.append(l.split(" ")[0])
    value.append(l.split(" ")[1])

for i in range(direction.__len__()):
    if direction[i] == "forward":
        position += int(value[i])
        depth += aim * int(value[i])
    elif direction[i] == "up":
        aim -= int(value[i])
    elif direction[i] == "down":
        aim += int(value[i])

print("Part 2: " + str(position*depth))