with open('day-3/input.txt', 'r') as f:
    input = f.read()

p_list = []

for pack in input.split('\n'):
    comp2 = pack[-int(len(pack)/2):]
    for i in pack:
        if i in comp2:
            x = ord(i)
            p_list+= [x - 96 if x > 96 else x - 38]
            break

print(f'Part one: {sum(p_list)}')