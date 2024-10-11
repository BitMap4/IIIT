from q1_a import pseudo_rand_num_gen
from random import random
from time import time

def rand1(seed, k):
    x = pseudo_rand_num_gen(int(float(seed)), k)
    l = len(str(int(seed)))|1
    return [i/(10**l) for i in x]

def rand2(_, k):
    return [random() for _ in range(k)]

if __name__ == '__main__':
    k = int(input("Enter number of coordinates: "))
    pi = []
    for f in (rand1, rand2):
        xy = f(time(), 2*k)
        x, y = xy[:k], xy[k:]
        inside = 0
        for i in range(k):
            inside += int(x[i]**2 + y[i]**2 < 1)
        pi.append((4*inside)/k)

    print(f"Pi calculated through:\n\tpseudo_random_num_gen: {pi[0]}\n\trandom.random: {pi[1]}")