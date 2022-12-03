with open('day-3/input.txt', 'r') as f:
    input = f.read()

p_list = []

for pack in input.split('\n'):  # split input into packs (lines)
    comp2 = pack[-int(len(pack)/2):]  # grab the last half of the line
    # go over each character in the line
    for i in pack: 
        if i in comp2:  # check for a match in the last half
            x = ord(i)  # convert to ascii # code (a = 97 A = 65)
            p_list += [x - 96 if x > 96 else x - 38]  # subtract to get the desired integer and add to list
            break

print(f'Part one: {sum(p_list)}')
