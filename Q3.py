ay_inputs_aight = []
with open('Q3_Input.txt') as t:
    for line in t:
        ay_inputs_aight.append(line.strip('\n'))

yo_directions_bruv = [s.split(" ")[0] for s in ay_inputs_aight]
yo_distances_bruv = [int(s.split(" ")[1]) for s in ay_inputs_aight]

fancy_directions_mate = zip(yo_directions_bruv , yo_distances_bruv)

forward = 0
depth = 0

for r, s in fancy_directions_mate:
    if r == 'forward':
        forward += s
    else:
        if r=='down':
            depth += s
        else:
            depth -= s

forward * depth

