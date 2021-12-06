input = open("inputs/1")
# 1st half: count increase between successive values
increase_count = 0
prev = float("inf")
for line in input.readlines():
    val = int(line)
    if val > prev:
        increase_count += 1
    prev = val
print(increase_count)

# 2nd half: count increase between sums of last 3 values
input.seek(0)
increase_count = 0
prev = float("inf")
vals = []
for line in input.readlines():
    val = int(line)
    vals.append(val)
    if len(vals) > 3:
        vals.pop(0)
    if len(vals) == 3:
        s = sum(vals)
        if s > prev:
            increase_count += 1
        prev = s
print(increase_count)