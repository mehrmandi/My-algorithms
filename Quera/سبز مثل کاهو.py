import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
inp = os.path.join(BASE_DIR, "input.txt")

DEBUG = os.path.exists(inp)

if DEBUG:
    sys.stdin = open(inp, "r")
    

def solve():
    data = sys.stdin.read().split() if DEBUG else sys.stdin.buffer.read().split()
    
    if not data:
        return
    
    it = iter(data)
    t = int(next(it))
    out = []
    
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        min_a = min(a)
        max_allow = 2 * min_a - 1
        
        res = 0

        for item in a:
            k = (item + max_allow - 1) // max_allow
            res += k - 1
            
        print(res)
        
        
if __name__ == "__main__":
    solve()       
