inputs = []
with open('Q5_Input.txt') as t:
    for line in t:
        inputs.append(line.strip('\n'))

most_common = ''
least_common = ''

for i in range(len(inputs[0])):

    one_tracker = 0
    
    for j in range(len(inputs)):
        if inputs[j][i] == '1':
            one_tracker += 1

    if one_tracker > len(inputs)*.5:
        most_common = most_common + '1'
        least_common = least_common + '0'
    else:
        most_common = most_common + '0'
        least_common = least_common + '1'

int(most_common,2) * int(least_common,2)
