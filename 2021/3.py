input = open("inputs/3")
# Part 1
words = []
for line in input.readlines():
    words.append(line)
bit_length = len(words[0])
one_counts = [0 for _ in range(bit_length)]

for word in words:
    for i in range(len(word)):
        if(word[i] == "1"):
            one_counts[i] += 1
gamma = 0
epsilon = 0
power = bit_length - 1
for one_count in one_counts:
    bit_val = 2 ** power
    if one_count > len(words) / 2:
        gamma += bit_val
    else:
        epsilon += bit_val
    power -= 1
print(gamma * epsilon)

# Part 2
def filter_words(words, cmp_fn):
    bit_length = len(words[0])
    for current_bit in range(bit_length):
        count = 0
        for word in words:
            if(word[current_bit] == "1"):
                count += 1
        if cmp_fn(count, len(words) / 2):
            selected_bit = "1" 
        else:
            selected_bit = "0"
        words = [word for word in words if word[current_bit] == selected_bit]
        if len(words) == 1:
            break
    return words[0]

oxygen_word = filter_words(words.copy(), lambda x, y: x >= y)
co2_word = filter_words(words.copy(), lambda x, y: x < y)

print(int(oxygen_word, 2) * int(co2_word, 2))