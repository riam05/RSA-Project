def inverse(e: int, totient: int ) -> int:
    """
    compute inverse using extended euclidean algo
    e in Z^*_(totient(N)) => e and totient coprime
    """
    a = totient
    b = e
    euclidsteps = []
    # forward run (Euclidean Algo)
    while b != 0:
        euclidsteps.append(a//b)
        new_a = b
        new_b = a%b
        a = new_a
        b = new_b
    # post-cond: a should be 1, since it's the gcd

    euclidsteps.pop()   
    # dump last step, and proceed backwards on previous steps
    # backward run
    u = 0
    v = 1
    for q in reversed(euclidsteps):
        new_u = v
        new_v = u-q*v
        u = new_u
        v = new_v

    return v%totient


def exp(e: int, c: int, mod: int) -> int:
    """
    double exponent in each iteration, 
    with respect to odd exponent e
    """
    base = c%mod
    result = 1

    while e > 0:
        rem = e%2 
        if rem == 1:
            result = (result*base)%mod
        base = (base*base)%mod
        e = e//2

    return result


def num_2_string(m: int) -> str:
    ch = []
    while m > 0:
        ch.append(encoding[m % 27])
        m = m//27
    ch.reverse()
    return "".join(ch)


def decrypt(p: int, q: int, e: int, c: int) -> str:
    """
    # compute e^(-1) in Z^*_(totient(N)) with call to inverse()
    # compute c^(e^-1) in Z^*_N in with call to exp()
    """
    N = p*q
    totient = (p-1)*(q-1)
    einv = inverse(e, totient)
    m = exp(einv, c, N)
    return num_2_string(m)


# encoding = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 
#             'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
#             'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21,
#             'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
encoding = " abcdefghijklmnopqrstuvwxyz" # 1-indexed


def encrypt(m_str: int, N: int, e: int) -> int:
    m = 0
    for ch in m_str:
        m = m*27+encoding.index(ch)

    return exp(e, m, N)


# test cases
# totient of 77 is (7-1)*(11-1)=60, and 13 is coprime to 60
c = encrypt("at", 77, 13)
print(decrypt(7, 11, 13, c))

P = 435958568325940791799951965387214406385470910265220196318705482144524085345275999740244625255428455944579
Q = 562545761726884103756277007304447481743876944007510545104946851094548396577479473472146228550799322939273
e = 7
c = 163077576587089932277514178989798339755826189700674110151160860819557757512053108465634676999401755817425637794522932574265893488854028596522889419543378155476439015236106447427921542963150735762104095795184542
print(decrypt(P, Q, 7, c))


    
