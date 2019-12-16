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

strings = FASTA_parse('rosalind_tran.txt')

a, b = strings.keys()
trans, transv = 0, 0
for i in range(len(strings[a])):
    if strings[a][i] == 'A':
        if strings[b][i] == 'G':
            trans += 1
        elif strings[b][i] == 'C' or strings[b][i] == 'T':
            transv += 1
    elif strings[a][i] == 'G':
        if strings[b][i] == 'A':
            trans += 1
        elif strings[b][i] == 'C' or strings[b][i] == 'T':
            transv += 1
    elif strings[a][i] == 'C':
        if strings[b][i] == 'T':
            trans += 1
        elif strings[b][i] == 'A' or strings[b][i] == 'G':
            transv += 1
    elif strings[a][i] == 'T':
        if strings[b][i] == 'C':
            trans += 1
        elif strings[b][i] == 'A' or strings[b][i] == 'G':
            transv += 1

print(trans/transv)