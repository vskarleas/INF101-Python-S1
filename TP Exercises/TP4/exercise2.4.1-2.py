def est_premier(N):
    i = 2
    a_diviseur=False
    while i<N and (not a_diviseur):
        if N%i==0:
            a_diviseur=True
        i = i+1
    
    return not a_diviseur

if __name__ == "__main__":
    rep=est_premier(9)
    print("9 est premier ?", rep)
    print("5 est premier ?", est_premier(5))

# Les variables locales de la fonction est_premier sont i et a_diviseur