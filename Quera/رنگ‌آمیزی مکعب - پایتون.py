def coloring(ls):
    m = len(ls)
    n = len(ls[0])
    nl = len(ls[0][0])
        
    for i in range(m):
        for j in range(n):    
            for k in range(nl):
                if i == 0 or i == m - 1:
                    ls[i][j][k] = 1
                
                else:
                    if j == 0 or j == n - 1:
                        ls[i][j][k] = 1
                    
                    else:
                        if k == 0 or k == nl - 1:
                            ls[i][j][k] = 1
                            
                        else:
                            ls[i][j][k] = 0  
                            
    pass
                    
            
    


