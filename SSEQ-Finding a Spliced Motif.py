with open('rosalind_sseq.txt') as f:
    text = f.read()
    items = text.split('>')
    s = ''.join(items[1].split('\n')[1:])
    t = ''.join(items[2].split('\n')[1:])

l = []
index = 0
for i in t:
    index = s.index(i, index) + 1
    l.append(index)

with open('rosalind_sseq_out.txt', 'w') as f:
    f.write(' '.join(map(str, l)))