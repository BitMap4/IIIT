from time import time

def pseudo_rand_num_gen(seed, k):
    """
    Returns a list of k pseudo-random numbers.
    """
    l = []
    k = int(k)
    initial_length = len(str(int(seed)))|1
    for _ in range(k):
        if int(seed) == 0: seed = k*time()
        while len(str(int(seed))) < initial_length:
            seed *= k+37
        seed = str(seed)[:initial_length]
        length = len(seed)
        seed = str(int(seed)**2).zfill(length*2)
        length = len(seed)
        seed = int(seed[length//4:length*3//4])
        l.append(seed)
    return l

if __name__ == '__main__':
    from matplotlib.pyplot import hist, show

    # print(x:=pseudo_rand_num_gen(t:=time(), input('Enter k: ')))
    x=pseudo_rand_num_gen(t:=time(), input('Enter k: '))

    hist([i/10**(len(str(int(t)))|1) for i in x], bins=10)
    show()