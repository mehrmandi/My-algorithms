from collections import Counter


def sameFreq(s):
    freq = Counter(s)                    # Count each character's frequency
    freq_values = list(freq.values())   # Get list of frequencies
    freq_count = Counter(freq_values)   # Count of each frequency

    if len(freq_count) == 1:
        # All frequencies are already the same
        return True
    elif len(freq_count) == 2:
        # Two different frequencies present
        key1, key2 = freq_count.keys()
        # Case 1: One character has frequency 1 and appears once (e.g., {'a': 1, 'b': 2, 'c': 2})
        if (freq_count[key1] == 1 and (key1 == 1 or key1 - key2 == 1)) or \
           (freq_count[key2] == 1 and (key2 == 1 or key2 - key1 == 1)):
            return True
    return False
    
        
        
        

s = "xyxyyzxz"
print(sameFreq(s))
