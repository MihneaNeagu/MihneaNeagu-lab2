def get_largest_prime_below(n):
    for i in range(n,1,-1):
        if div(i)==0:
            return i
    return None
def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(100) == 97 
    assert get_largest_prime_below(17) == 17
    assert get_largest_prime_below(250) == 241
    assert get_largest_prime_below(1000) == 997
    assert get_largest_prime_below(1) == None

    print("Toate bune")
def div(a):
    nrdiv=0
    for i in range(2,a//2+1):
        if a%i==0:
            nrdiv+=1
    return nrdiv

while True:
    print("1. Problema 1")
    print("2. Problema 2")
    comanda = input("Comanda: ")
    if comanda == "1":
        n = input("N=")
        print(get_largest_prime_below(int(n)))

vector = [31,28,31,30,31,30,31,31,30,31,30,31]
def days_up_to_date(x,y):
    days=0
    for i in range(0,y-1):
        days+=vector[i]
    days+=x
    return days
def get_age_in_days(zi,luna,an):
    zile=0
    for i in range(2020,an,-1):
        if i%4==0:
            zile+=366
        else:
            zile+=365
    zile+= days_up_to_date(5,10)
    if an%4==0:
        zile+=366-days_up_to_date(zi,luna)
    else:
        zile+=365-days_up_to_date(zi,luna)
    return zile
    
def test_get_age_in_days():
    assert get_age_in_days(2,1,2003) == 6851

def is_antipalindrome(n):
    aux=n
    inv=0
    nrcf=0
    while aux:
        nrcf+=1
        inv=inv*10+aux%10
        aux=aux//10
    ok=1
    if nrcf%2==0:
        if n%10==inv%10:
            ok=0
        n=n/10
        inv=inv/10
    else:
        nrcf=nrcf/2-1
        while nrcf:
            if n%10==inv%10:
                ok=0
                nrcf-=1
    if ok==1:
        return "Da"
    else:
        return "Nu"
def test_is_antipalindrome():
    assert is_antipalindrome(6776)=="Nu"
    assert is_antipalindrome(66778)=="Da"





