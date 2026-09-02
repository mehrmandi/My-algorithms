# A cafe has n computers. The customer events are represented by a string s of uppercase English letters, where each distinct letter appears exactly twice:

# The first occurrence denotes the customer's arrival.
# The second occurrence denotes the customer's departure.
# A customer is assigned a computer only if one is available at the time of arrival, otherwise the customer is rejected and does not use a computer.

# Return the number of customers who could not be assigned a computer upon arrival.



def solve(n, s):
    state = [0] * 26
    occupied = 0
    rejected = 0

    for c in s:
        i = ord(c) - ord('A')

        if state[i] == 0:          # arrival
            if occupied < n:
                occupied += 1
                state[i] = 1       # accepted
            else:
                rejected += 1
                state[i] = 2       # rejected

        elif state[i] == 1:        # departure of accepted customer
            occupied -= 1
            state[i] = 0

        else:                      # departure of rejected customer
            state[i] = 0

    return rejected



n = 1
s = "ABCBAC"
print(solve(n, s))
            
        
