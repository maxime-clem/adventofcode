input = open("inputs/5")
lines = []
max_x = 0
max_y = 0
for line in input.readlines():
  start, end = line.split(' -> ')
  start_x, start_y = start.split(',')
  end_x, end_y = end.split(',')
  start = [int(start_x), int(start_y)]
  end = [int(end_x), int(end_y)]
  max_x = max(max_x, start[0], end[0])
  max_y = max(max_y, start[1], end[1])
  lines.append([start, end])

# Part 1
overlaps = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for line in lines:
    if line[0][0] == line[1][0]:
        from_y = min(line[0][1], line[1][1])
        to_y = max(line[0][1], line[1][1])
        for y in range(from_y, to_y + 1):
            overlaps[line[0][0]][y] += 1
    elif line[0][1] == line[1][1]:
        from_x = min(line[0][0], line[1][0])
        to_x = max(line[0][0], line[1][0])
        for x in range(from_x, to_x + 1):
            overlaps[x][line[0][1]] += 1

count = 0
for row in overlaps:
    for overlap in row:
        if overlap >= 2:
            count += 1
print(count) 

# Part 2
overlaps = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for line in lines:
    from_y = min(line[0][1], line[1][1])
    to_y = max(line[0][1], line[1][1])
    from_x = min(line[0][0], line[1][0])
    to_x = max(line[0][0], line[1][0])
    if from_x == to_x:
        for y in range(from_y, to_y + 1):
            overlaps[line[0][0]][y] += 1
    elif from_y == to_y:
        for x in range(from_x, to_x + 1):
            overlaps[x][line[0][1]] += 1
    else:
        increment_x = 1 if line[0][0] < line[1][0] else -1
        increment_y = 1 if line[0][1] < line[1][1] else -1
        # diagonal case
        for x, y in zip(range(line[0][0], line[1][0] + increment_x, increment_x), range(line[0][1], line[1][1] + increment_y, increment_y)):
            overlaps[x][y] += 1


count = 0
for row in overlaps:
    for overlap in row:
        if overlap >= 2:
            count += 1
print(count) 