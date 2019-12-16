def FASTA_parse(file):
    strings = []
    with open(file) as f:
        text = f.read()
        items = text.split('>')
    for item in items[1:]:
        item = item.split('\n')
        item.pop(0)
        strings.append(''.join(item))
    return strings

def hamm(s, t):
    d_h = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            d_h += 1
    return d_h

strings = FASTA_parse('rosalind_pdst.txt')
n = len(strings)
D = [[None]*n for i in range(n)]
l = len(strings[0])
for i in range(n):
    for j in range(i, n):
        d_p = hamm(strings[i], strings[j]) / l
        D[i][j], D[j][i] = d_p, d_p

with open('rosalind_pdst_out.txt', 'w') as f:
    for i in range(n):
        f.write(' '.join(map(str, D[i]))+'\n')
        