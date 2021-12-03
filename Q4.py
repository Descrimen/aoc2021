inputs = []
with open('Q3_Input.txt') as t:
    for line in t:
        inputs.append(line.strip('\n'))

yo_directions_bruv = [s.split(" ")[0] for s in inputs]
yo_distances_bruv = [int(s.split(" ")[1]) for s in inputs]

fancy_directions_mate = zip(yo_directions_bruv , yo_distances_bruv)

aim_tracka = 0
forward = 0
depth = 0

for r, s in fancy_directions_mate:
    if r == 'forward':
        forward += s
        depth += (aim_tracka * s)
    else:
        if r=='down':
            aim_tracka += s
        else:
            aim_tracka -= s

forward * depth