with open('rosalind_hamm.txt') as f:
    s = f.readline().strip()
    t = f.readline().strip()
d_h = 0
for i in range(len(s)):
    if s[i] != t[i]:
        d_h += 1
print(d_h)