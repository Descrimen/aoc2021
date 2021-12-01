# Today I will be writing the code yes.
ay_numbahs_aight = []
with open('Q1_Input.txt') as t:
    for line in t:
        ay_numbahs_aight.append(int(line.strip('\n')))

ay_just_a_counter_aight = 0

for n in range(len(ay_numbahs_aight)-1):
    if ay_numbahs_aight[n+1] > ay_numbahs_aight[n]:
        ay_just_a_counter_aight = ay_just_a_counter_aight + 1 

ay_just_a_counter_aight