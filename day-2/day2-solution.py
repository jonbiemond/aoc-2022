with open('day-2/input.txt', 'r') as f:
    input = f.read()

input = input[:39].strip()
print([i for i in input.split('\n')])

# convert to integers by getting the ASCII value
result = [(ord(i[0])-63, ord(i[-1])-87) for i in input.split('\n')]

# come up with some fancy math...

