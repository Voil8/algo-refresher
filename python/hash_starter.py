
from linked_list import *

class HSET:
    '''hash sets'''
    def __init__(self, m=20, big_prime=1000013):
        self.store = [LinkedList() for i in range(m)]
        self.m = m
        self.bp = big_prime

    def ah(self, number, a=34, b=2):
        return ((a*number + b) % self.bp) % self.m

    def is_in(self, number):
        hash_ = self.ah(number)
        return self.store[hash_].find_node_(number) is not None

    def add(self, number):
        # print(f'adding {number}')
        if not self.is_in(number):
            hash_  = self.ah(number)
            # print(f'calculated_hash {hash_}')
            self.store[hash_].push_back(Node(number))

    def remove(self, number):
        if self.is_in(number):
            hash_ = self.ah(number)
            self.store[hash_].remove(number)

class StringHash(HSET):
    def ah(self, string='', a=31,):
        h_ = 0
        for i, s in enumerate(string):
            h_ += ord(s)*(a**i) % self.bp
        return h_ % self.m



if __name__ == '__main__':
    import random


    c = """
    s = random.choices(range(900), k=20)

    print(s)

    set_ = HSET()
    for i in s:
        set_.add(i)

    
    print(f'''Check few \n{s[-1]} in set?:Ans: True, Returned: {set_.is_in(s[-1])} 
    {s[4]} in set?:Ans: True, Returned: {set_.is_in(s[-1])} 
    {s[-7]} in set?:Ans: True, Returned: {set_.is_in(s[-1])}''')

    print()
    print([i.len for i in set_.store])

    to_remove = (s[6], s[4], s[0], s[12])


    print(f'removing few, {to_remove}')
    for i in to_remove:
        set_.remove(i)

    print('checking removed ones')
    for i in to_remove:
        print(f'is_in {i}', set_.is_in(i))

    print([i.len for i in set_.store])"""

    s_to_hash = [
        "Ravi",
        "Raman",
        "Harish",
        "vishal",
        "Vishal",
    ]

    print(s_to_hash)

    s_hash = StringHash()
    s_hash.add("Raman")
    s_hash.add("Harish")
    print('False:', s_hash.is_in("Raghav"))
    print('True:', s_hash.is_in("Harish"))

    s_hash.add('Vishal')
    print('False:', s_hash.is_in('vishal'))
    # s_hash.remove('Vishal')
    s_hash.remove('vishal')
    print('False:', s_hash.is_in('Vishal'))
    print(s_hash.store)





