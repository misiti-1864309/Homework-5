from itertools import permutations

with open('rosalind_perm.txt') as f:
    n = int(f.readline())

with open('rosalind_perm_out.txt', 'w') as f:
    perms = list(permutations(range(1, n+1)))
    f.write(str(len(perms))+'\n')
    for i in perms:
        f.write(' '.join(map(str, i))+'\n')