import sys
import numpy as np

mismatch_cost = {
    'AA':0, 'AC':110, 'AG':48, 'AT':94,
    'CA':110, 'CC':0, 'CG':118, 'CT':48,
    'GA':48, 'GC':118, 'GG':0, 'GT':110,
    'TA':94, 'TC':48, 'TG':110, 'TT':0
}

gap_penalty = 30

def find_alignment_cost(X_aligned, Y_aligned):
    cost = 0.0
    for i in range(len(X_aligned)):
        if X_aligned[i] == '_' or Y_aligned[i] == '_':
            cost += 30.0
        else:
            cost += mismatch_cost[X_aligned[i] + Y_aligned[i]]
    return cost

''' DP Optimal Alignment Cost '''
def get_alignment_cost(string1, string2):
    #Optimal Alignment Table (N+1 x M+1)
    alignment_cost = np.zeros((len(string1)+1,len(string2)+1))

    # Intialization with gap_penalities
    for r in range(1,len(alignment_cost)):
        alignment_cost[r,0] = gap_penalty * r
    for c in range(1,len(alignment_cost[0])):
        alignment_cost[0,c] = gap_penalty * c
    alignment_cost[0,0] = 0

    # selecting the best possible cost out of the three possible moves
    for r in range(1,len(string1)+1):
        for c in range(1,len(string2)+1):
            both_matched = alignment_cost[r-1,c-1]+mismatch_cost[string1[r-1]+string2[c-1]]
            string1_not_matched = alignment_cost[r-1,c]+gap_penalty
            string2_not_matched = alignment_cost[r,c-1]+gap_penalty
            alignment_cost[r,c] = min(both_matched,string1_not_matched,string2_not_matched)
    # print("alignment cost :{0}".format(alignment_cost[-1][-1]))
    return alignment_cost

''' DP Optimal Alignment '''
def get_alignment(string1, string2):
    alignment_cost = get_alignment_cost(string1, string2)
    string1_aligned = ''
    string2_aligned = ''
    r, c = len(string1), len(string2)
    cost = alignment_cost[r, c]
    memory = sys.getsizeof(alignment_cost)

    while r>0 and c>0:
        # 3 possible moves represented as a tuple (move,cost)
        possible_moves = [((r-1,c-1),alignment_cost[r-1,c-1]), ((r-1,c),alignment_cost[r-1,c]), ((r,c-1),alignment_cost[r,c-1])]
        # finds the minimum cost out of the 3 possible moves on the basis of cost, and returns the move
        previous_move = min(possible_moves, key = lambda x:x[1])[0]

        ''' Three conditions possible: -
            1. matched letters in both string
            2. no match for string1 letter - add gap in string2
            3. no match for string2 letter - add gap in string1 '''
        if previous_move[0] == r-1 and previous_move[1] == c-1:
            string1_aligned += string1[r-1]
            string2_aligned += string2[c-1]
            r -= 1
            c -= 1
        elif previous_move[0] == r-1:
            string1_aligned += string1[r-1]
            string2_aligned += '_'
            r -= 1
        else:
            string1_aligned += '_'
            string2_aligned += string2[c-1]
            c -= 1

    ''' if any one of the string did not reach end add gaps in the other string'''
    while r!=0:
        string1_aligned += string1[r-1]
        string2_aligned += '_'
        r-=1
    while c!=0:
        string2_aligned += string2[c-1]
        string1_aligned += '_'
        c-=1

    return string1_aligned[::-1], string2_aligned[::-1], cost, memory







''' Memory Efficient Optimal Alignment'''
def get_alignment_efficient(string1, string2):
    string1_alignment_me, string2_alignment_me = get_alignment_me(string1,string2)
    cost = find_alignment_cost(string1_alignment_me, string2_alignment_me)
    memory_cost = np.zeros((2,len(string2)+1))
    memory = sys.getsizeof(memory_cost)

    return string1_alignment_me, string2_alignment_me, cost, memory

def get_alignment_me(string1, string2):
    # if any string is having only 2 letters, call the normal DP solution
    if len(string1)<=2 or len(string2)<=2:
        string1_aligned, string2_aligned, cost_dummy, memory_dummy = get_alignment(string1,string2)
        return string1_aligned, string2_aligned

    ''' Divide Step '''
    # break string1 in half
    string1_left, string1_right = string1[:int(len(string1)/2)], string1[int(len(string1)/2):]

    # get alignment cost of string1_left with the whole of string2
    alignment_cost_left = get_alignment_cost_me(string1_left,string2)
    # get alignment cost of string1_right reversed with string2 reversed
    alignment_cost_right = get_alignment_cost_me(string1_right[::-1],string2[::-1])

    # find the optimal break point for string2
    min = np.inf
    for c in range(0,len(string2)):
        if min > alignment_cost_left[0,c] + alignment_cost_right[0,len(string2)-c]:
            min = alignment_cost_left[0,c] + alignment_cost_right[0,len(string2)-c]
            string2_break_point = c

    ''' Conquer Step: -
        recursively repeat the process for the string1_left and string2[0:breakpoint]
        recursively repeat the process for the string1_right and string2[breakpoint:-1] '''
    string1_left_aligned, string2_left_aligned = get_alignment_me(string1_left,string2[:string2_break_point])
    string1_right_aligned, string2_right_aligned = get_alignment_me(string1_right,string2[string2_break_point:])

    '''Combine Step - add the optimal alignments found '''
    string1_aligned = string1_left_aligned + string1_right_aligned
    string2_aligned = string2_left_aligned + string2_right_aligned

    return string1_aligned, string2_aligned

''' Memory Efficient Optimal Alignment Cost '''
def get_alignment_cost_me(string1, string2):
    # Optimal Alignment Table (N+1 x 2)
    alignment_cost = np.zeros((2,len(string2)+1))

    alignment_cost[0,0] = 0
    # Initialize with gap penalties
    for c in range(1,len(alignment_cost[0])):
        alignment_cost[0,c] = gap_penalty * c

    for r in range(1,len(string1)+1):
        for c in range(0,len(string2)+1):
            # intialize 1st column with gap penalty
            if c==0:
                alignment_cost[1,0] = gap_penalty*r
                continue
            # selecting the best possible cost out of the three possible moves
            both_matched = alignment_cost[0,c-1]+mismatch_cost[string1[r-1]+string2[c-1]]
            string1_not_matched = alignment_cost[0,c]+gap_penalty
            string2_not_matched = alignment_cost[1,c-1]+gap_penalty
            alignment_cost[1,c] = min(both_matched,string1_not_matched,string2_not_matched)

        # updating the top row with the updated values
        alignment_cost[0,:] = alignment_cost[1,:]

    return alignment_cost