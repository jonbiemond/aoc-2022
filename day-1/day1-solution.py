import pandas as pd

with open('day-1/input.txt', 'r') as f:
    input = f.read()

# use a pandas.Series because fancy hashmap
ser = pd.Series([sum([int(i) for i in s.split('\n')]) for s in input.strip().split('\n\n')]).sort_values(ascending=False)
print(f'Part one: {ser[:1]}')
print(f'Part two: {ser[:3].sum()}')

# built-ins only approach
i = input.strip().split('\n\n')
cal_list = sorted(map(lambda x: sum(map(int, x.split("\n"))), i))[::-1]
