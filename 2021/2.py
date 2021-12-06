input = open("inputs/2")

### 1st half
# count horizontal and depth moves
horizontal = 0
depth = 0
for line in input.readlines():
    move, dist = line.split()
    if move == "forward":
        horizontal += int(dist)
    elif move == "down":
        depth += int(dist)
    elif move == "up":
        depth -= int(dist)
# result is horizontal * depth
print(horizontal * depth)

### 2nd half
input.seek(0)

horizontal = 0
depth = 0
aim = 0
for line in input.readlines():
    move, dist = line.split()
    if move == "forward":
        horizontal += int(dist)
        depth += aim * int(dist)
    elif move == "down":
        aim += int(dist)
    elif move == "up":
        aim -= int(dist)

print(horizontal * depth)