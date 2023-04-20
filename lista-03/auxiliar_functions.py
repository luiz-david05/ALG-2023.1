def eh_par(n): return n % 2 == 0

def eh_multiplo(n1, n2): return n1 % n2 == 0

def eh_primo(n):
    if n <= 1:
        return False
    
    i = 2

    while i < n:
        if eh_multiplo(n, i):
            return False
        
        i += 1

    return True