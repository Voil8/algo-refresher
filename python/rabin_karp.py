'''
Goal: given, T:text and P:pattern,
find all i such that T[i:i+|p|] == P

in O(N) time
'''
prime = 104729
x = 31

def poly_hash(P):
    global prime, x
    h_ = 0
    for i, j in enumerate(P):
        h_ += ord(j) * x**i % prime 
    return h_

def preCompute(T, l):
    global prime, x
    len_ = len(T)-l
    H = [0] * len_
    tHash = poly_hash(T[-l:])
    y=1
    for i in range(len_):
        y *= y % prime

    H[len_-1] = tHash
    for i in range(len_-1)[::-1]:
        H[i] = (ord(T[i]) + x * H[i+1] - y*ord(T[i+l]) ) % prime

    return H

    
def areEqual(a, b):
    return len(a) == len(b) and all([a[i]==b[i] for i in range(len(a))])

def rabin_karp(T, P):    
    results = []
    pHash = poly_hash(P)
    l = len(P)
    len_ = len(T) - l
    H = [0]*len_
    
    tHash = preCompute(T, len(P))
    for i in range(len_):
        if tHash[i] == pHash:
            continue
        elif areEqual(T[i:i+l], P):
            results.append(i)
    return results


def test():
    tt1 = 'so hello from the other side, at least i can see then I tried!'
    pp11 = 'r sid'
    pp12 = 'ea'    

    tt2 = 'aaaaaaaabaaaabaabaabaa'
    pp21 = 'aaaa'
    pp22 = 'aaabaa'
    
    tl = [(tt1, pp11), (tt1, pp12), (tt2, pp21), (tt2, pp22)]
    for tt, pp in tl:
        print(f'T:{tt}, P:{pp}\n{[(i, tt[i:i+len(pp)]) for i in rabin_karp(tt, pp)]}\n')

if __name__ == '__main__':
    test()






    
