def est_premier(N):
    i = 2
    if N > 0:
        while i < N and N % i != 0:
            i = i +1
        if i == N :
            est_premier = True
        else :
            est_premier = False
    return est_premier

def plus_grand_diviseur_premier(n):
    largest_divisor = 0
    listing =[]
    for i in range(2, n):
        if n % i == 0:
            N = i
            cap = est_premier(N)
            if cap == True:
                largest_divisor = i
                listing.append(largest_divisor)
    return listing

def pgcd(a , b):
    o=1
    n = a
    alfa = plus_grand_diviseur_premier(n)
    n = b
    lamda = plus_grand_diviseur_premier(n)
    if len(alfa)>len(lamda):
        h = len(lamda)
    elif len(alfa)<len(lamda):
        h = len(alfa)
    else:
        h = len(alfa)

    for k in range(0, h):
        if alfa[o-1:o:1] == lamda[o-1:o:1]:
            commun = alfa[o-1:o:1]
        o = o + 1
    return commun[0]

def ppcm(a , b):
    o=1
    n = a
    alfa = plus_grand_diviseur_premier(n)
    n = b
    lamda = plus_grand_diviseur_premier(n)
    if len(alfa)>len(lamda):
        h = len(lamda)
    elif len(alfa)<len(lamda):
        h = len(alfa)
    else:
        h = len(alfa)
    
    list1_as_set = set(alfa)
    intersection = list1_as_set.intersection(lamda)
    intersection_as_list = list(intersection)
    minimum = min(intersection_as_list)
    return minimum

def irreductible(numerator, denominator):
    if denominator != 0:
        uta = pgcd(a, b)
        if uta != (numerator/denominator):
            iota = numerator/denominator
            if iota == 1:
                return True
            else:
                return False
        else:
            return True

#Main program
a = int(input("Give a first number to find the bigest divider: "))
b = int(input("Give a second number to find the bigest divider: "))
numerator = a
denominator = b
if a != 0 and b !=0:
    print(pgcd(a, b))
    print(ppcm(a, b))
    print(irreductible(numerator, denominator))

