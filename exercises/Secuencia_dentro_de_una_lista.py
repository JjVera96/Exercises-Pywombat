def max_seq(sequence):
    i = 0
    max_len = 0
    init_sequence = 0
    while(i < len(sequence)):
        length = 0
        init = i
        while(True): 
            if(i+1<len(sequence) and sequence[i] + 1 == sequence[i + 1]):
                i += 1
                length +=1
            else: 
                i +=1
                break
        if(max_len < length): 
            max_len = length
            init_sequence = init 
    return sequence[init_sequence:init_sequence + max_len + 1] if max_len else []
        
print(max_seq(  [10, 11, 12, 1, 4, 5, 6, 7, 8, 9, 13, 14, 100, 101] ))
print(max_seq( [1, 2, 3, 5, 6, 10, 12, 14] ))
print(max_seq( [1, 3, 4, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16] ))
print(max_seq( [10, 20, 30, 40, 50, 60] ))