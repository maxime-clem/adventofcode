input = open("inputs/4")
# Part 1
numbers = [int(i) for i in input.readline().split(',')]  # 1st line is the drawn numbers
# grids are in row-column format
grids = []
curr_grid = []
for line in input.readlines():
    if len(line.strip()) == 0:
        if curr_grid:
            grids.append(curr_grid)
            curr_grid = []
        continue
    curr_grid.append([int(i) for i in line.split()])

def bingo():
    matches = [[[False for _ in range(5)] for _ in range(5)] for _ in grids]
    for number in numbers:
        for grid, match in zip(grids, matches):
            for i in range(5):
                for j in range(5):
                    if grid[i][j] == number:
                        match[i][j] = True
                        if all(match[i]) or all([match[x][j] for x in range(5)]):
                            score = sum([grid[x][y] for x in range(5) for y in range(5) if not match[x][y]])
                            return score * number
print(bingo())

# Part 2

def bingo2():
    matches = [[[False for _ in range(5)] for _ in range(5)] for _ in grids]
    wins = [False for _ in grids]
    for number in numbers:
        for n, grid, match in zip(range(len(grids)), grids, matches):
            for i in range(5):
                for j in range(5):
                    if grid[i][j] == number:
                        match[i][j] = True
                        if all(match[i]) or all([match[x][j] for x in range(5)]):
                            wins[n] = True
                            if all(wins):
                                score = sum([grid[x][y] for x in range(5) for y in range(5) if not match[x][y]])
                                return score * number
print(bingo2())
