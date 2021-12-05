from tqdm import tqdm

inputs = []

with open('Q9_Input.txt') as t:
    for line in t:
        inputs.append(line.strip('\n'))

x1 = [int(x.split(' -> ')[0].split(',')[0]) for x in inputs]
x2 = [int(x.split(' -> ')[1].split(',')[0]) for x in inputs]
y1 = [int(x.split(' -> ')[0].split(',')[1]) for x in inputs]
y2 = [int(x.split(' -> ')[1].split(',')[1]) for x in inputs]

coords = list(zip(x1, y1, x2, y2))

straight_lines = [c for c in coords if (c[0]==c[2] or c[1]==c[3])]

ordered_x_coords = [(c[2], c[1], c[0], c[3]) if (c[2] < c[0]) else c for c in straight_lines]
ordered_coords = [(c[0], c[3], c[2], c[1]) if (c[3] < c[1]) else c for c in ordered_x_coords]

full_ranges = [list(zip(range(x[0],x[2]+1),[x[1]]*(x[2]-x[0]+1))) if (x[1]==x[3]) else list(zip([x[0]]*(x[3]-x[1]+1),range(x[1],x[3]+1))) for x in ordered_coords]
all_points = [a for b in full_ranges for a in b]

def count_the_points(coordlist):
    counts = []
    in_the_counter = []
    for coord in coordlist:
        if coord in in_the_counter:
            counts[in_the_counter.index(coord)] = counts[in_the_counter.index(coord)] + 1
        else:
            counts.append(1),
            in_the_counter.append(coord)
    return list(zip(in_the_counter,counts))


for x in tqdm(all_points):
    a = all_points.count(x)

counts = count_the_points(all_points)
len([x for x in counts if x[1] > 1])
