def string_matching(string, pattern):
    a = len(string)
    b = len(pattern)
    #base to be 10
    pattern_hash = sum([ord(pattern[i])*(10**(b-i-1)) for i in range(b)])
    
    rolling_hash = []
    
    for i in range(a-b+1):
        if i == 0:
            rolling_hash = [ord(string[i])*(10**(b-i-1)) for i in range(b)]
            rolling_hash_sum = sum(rolling_hash)
                
        else:
            rem = rolling_hash.pop(0)
            rolling_hash = [i*10 for i in rolling_hash]
            rolling_hash.append(ord(string[i+b-1]))
            rolling_hash_sum = 10*(rolling_hash_sum - rem) + rolling_hash[-1]
            
        if rolling_hash_sum == pattern_hash:
            print("Pattern matches at index " + str(i))