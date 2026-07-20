n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))


def reversion(arr, n):
    count = [0 for _ in range(max(arr) + 1)]
    count[arr[0]] = 1
    res = 0
    
    for i in range(1, n):
        res += sum(count[arr[i] + 1:])
        count[arr[i]] += 1
        
    return res % 100000

print(reversion(arr, n))
        
        
    


