inputs = []
with open('Q5_Input.txt') as t:
    for line in t:
        inputs.append(line.strip('\n'))

adjustable_inputs_m = [x for x in inputs]
adjustable_inputs_l = [x for x in inputs]

for i in range(len(inputs[0])):

    one_tracker = 0
    zero_tracker = 0

    for j in range(len(adjustable_inputs_m)):
        if adjustable_inputs_m[j][i] == '1':
            one_tracker += 1
        else:
            zero_tracker += 1

    if one_tracker >= zero_tracker:
        most_common = '1'
    else:
        most_common = '0'
        
    adjustable_inputs_m = [x for x in adjustable_inputs_m if x[i] == most_common]

    if len(adjustable_inputs_m) == 1:
        break

for i in range(len(inputs[0])):

    zero_tracker = 0
    one_tracker = 0

    for j in range(len(adjustable_inputs_l)):
        if adjustable_inputs_l[j][i] == '0':
            zero_tracker += 1
        else:
            one_tracker += 1

    if zero_tracker <= one_tracker:
        least_common = '0'
    else:
        least_common = '1'
    
    adjustable_inputs_l = [x for x in adjustable_inputs_l if x[i] == least_common]

    if len(adjustable_inputs_l) == 1:
        break

int(adjustable_inputs_l[0],2) * int(adjustable_inputs_m[0],2)
