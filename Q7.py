inputs = []

with open('Q7_Input.txt') as t:
    for line in t:
        inputs.append(line.strip('\n'))

callouts = inputs[0].split(',')

boards = inputs[1:]
boards = [list(filter(None,s.split(' '))) for s in boards if s!='']
boards = [[boards[n],boards[n+1],boards[n+2],boards[n+3],boards[n+4]] for n in range(0, len(boards), 5)]

def BINGO(five_lists):
    #rows
    for i in range(5):
        if five_lists[i] == [-1,-1,-1,-1,-1]:
            return five_lists

    #columns
    transposed = list(map(list, zip(*five_lists)))
    for i in range(5):
        if transposed[i] == [-1,-1,-1,-1,-1]:
            return five_lists

    #diagonals
    diagonal_tl_br = [five_lists[i][i] for i in range(5)]
    diagonal_bl_tr = [five_lists[i][4-i] for i in range(5)]

    if (diagonal_tl_br == [-1,-1,-1,-1,-1]) or (diagonal_bl_tr == [-1,-1,-1,-1,-1]):
        return five_lists
    
    return False

def mark_the_boards(boards, marker):
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for s in range(len(boards[board][row])):
                    if marker == boards[board][row][s]:
                        boards[board][row][s] = -1

for number in callouts:
    mark_the_boards(boards, number)

    for board in boards:

        the_one = False
        the_one = BINGO(board)

        if the_one != False:
            break

    if the_one!= False:
        break

all_unmarked = [int(x) for r in the_one for x in r if type(x)==str]
sum(all_unmarked) * int(number)