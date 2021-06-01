import numpy as np
def crazy8(sequence):
    seq = sequence
    a = len(seq)
    arr = np.zeros(a)
    arr[0] = 1
    pattern = []
    i = 1
    
    while i<a:
                
        if seq[i][:2] == '10':
            if len(seq[i-1]) == 2:
                if (seq[i][2].lower() == seq[i-1][1].lower()):
                    arr[i] = 1+max(arr[:i])
                    
                else:
                    arr[i] = arr[i-1]
                    
            elif len(seq[i-1]) == 3:
                if (seq[i][2].lower() == seq[i-1][2].lower()) or (seq[i][:2] == seq[i-1][:2]):
                    arr[i] = 1+max(arr[:i])
                    
                else:
                    arr[i] = arr[i-1]
                    
        elif seq[i-1][:2] == '10':
            if len(seq[i]) == 2:
                if (seq[i][1].lower() == seq[i-1][2].lower()):
                    arr[i] = 1+max(arr[:i])
                    
                else:
                    arr[i] = arr[i-1]
                    
            elif len(seq[i]) == 3:
                if (seq[i][2].lower() == seq[i-1][2].lower()) or (seq[i][:2] == seq[i-1][:2]):
                    arr[i] = 1+max(arr[:i])
                    
                else:
                    arr[i] = arr[i-1]
                    
                    
        elif seq[i][1].lower() in 'chds':
            if (seq[i][1].lower() == seq[i-1][1].lower()) or (seq[i][0] == seq[i-1][0]) or (seq[i][0] == '8'):
                arr[i] = 1+max(arr[:i])
                
            else:
                arr[i] = arr[i-1]
                
        else:
            print(seq[i] + 'Not a valid entry for the deck')
            seq.pop(i)
            a -= 1
            if (seq[i][1].lower() == seq[i-1][1].lower()) or (seq[i][0] == seq[i-1][0]) or (seq[i][0] == '8'):
                arr[i] = 1+max(arr[:i])
                
            else:
                arr[i] = arr[i-1]
                
        i += 1
    
    for i in range(1,len(np.unique(arr))+1):
        pattern.append(seq[np.where(arr == i)[0][-1]])
    
    print('length of longest subsequence is: ', max(arr))
    print('Pattern corresponding to longest subsequence is: ', pattern)

crazy8(['7c', '7h', 'kc', 'ks', '8h'])