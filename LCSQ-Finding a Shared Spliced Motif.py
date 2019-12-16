def FASTA_parse(file):
    strings = {}
    with open(file) as f:
        text = f.read()
        items = text.split('>')
    for item in items[1:]:
        item = item.split('\n')
        string_id = item.pop(0)
        strings[string_id] = ''.join(item)
    return strings

s, t = FASTA_parse('rosalind_lcsq.txt').values()

def LCS(v, w):
    n, m = len(v), len(w)
    s = [[None] * (m+1) for i in range(n+1)]
    b = [[None] * (m+1) for i in range(n+1)]
    for i in range(0, n+1):
        s[i][0] = 0
    for j in range(1, m+1):
        s[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if v[i-1] == w[j-1]:
                s[i][j] = s[i-1][j-1] + 1
                b[i][j] = '\\'
            else:
                k, l = s[i-1][j], s[i][j-1]
                if k >= l:
                    s[i][j] = k
                    b[i][j] = '|'
                else:
                    s[i][j] = l
                    b[i][j] = '-'
    return s[n][m], b


lcs = []
def printLCS(b, v, i, j):
    if i == 0 or j == 0:
        return
    elif b[i][j] == '\\':
        printLCS(b,v,i-1,j-1)
        lcs.append(v[i-1])
    elif b[i][j] == '|':
        printLCS(b,v,i-1,j)
    else:
        printLCS(b,v,i,j-1)

b = LCS(s, t)[1]
printLCS(b, s, len(s), len(t))
with open('rosalind_lcsq_out.txt', 'w') as f:
    f.write(''.join(lcs))