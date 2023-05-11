def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
    
print(factorielle(4)) # 4*3*2*1