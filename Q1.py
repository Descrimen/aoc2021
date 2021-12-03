# Today I will be writing the code yes.
inputs = []
with open('Q1_Input.txt') as t:
    for line in t:
        inputs.append(int(line.strip('\n')))

simple_counter = 0

for n in range(len(inputs)-1):
    if inputs[n+1] > inputs[n]:
        simple_counter = simple_counter + 1 

simple_counter