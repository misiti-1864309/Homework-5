with open('rosalind_tree.txt') as f:
    n = int(f.readline())
    adj = f.readlines()

print(n-1-len(adj))