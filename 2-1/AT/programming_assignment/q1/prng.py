def test():
    n, m, current, size = [int(x) for x in input().split()]
    transitions = {}
    i=0
    while i<m:
        a, b = [int(x) for x in input().split()]
        transitions[a] = b
        i += 1

    visited = [0] * (n+1)
    loop_start = -1
    loop_end = False
    loop_length = 0
    i=0
    while i<size:
        if visited[current]:
            if loop_start == current:
                loop_end = True
                break
            elif loop_start == -1:
                loop_start = current
            loop_length += 1
        visited[current] += 1
        # print(current, visited[current]) #! remove
        current = transitions[current]
        i += 1
    
    if loop_end:
        remaining = size - i
        i=0
        while i<loop_length:
            visited[current] += remaining // loop_length
            # print(current, visited[current]) #! remove
            current = transitions[current]
            i += 1
        remaining = remaining % loop_length
        i=0
        while i<remaining:
            visited[current] += 1
            # print(current, visited[current]) #! remove
            current = transitions[current]
            i += 1

    print(' '.join([str(x) for x in visited[1:]]))

t = int(input())
i=0
while i<t:
    test()
    i += 1