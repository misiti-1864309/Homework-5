with open('DNA codon table.txt') as f:
    text = f.read().split()
code = {}
for i in range(0, len(text), 2):
    code[text[i]] = text[i+1]

with open('rosalind_orf.txt') as f:
    text = f.read()
    items = text.split('>')
    item = items[1].split('\n')
    string_id = item.pop(0)
    s = ''.join(item)

def find_ORFs(s):
    ORFs = []
    j = 0
    while True:
        j = s.find('ATG', j+1)
        if j == -1:
            break
        else:
            prot = []
            for i in range(j, len(s)-2, 3):
                codon = s[i:i+3]
                if code[codon] == 'Stop':
                    ORFs.append(''.join(prot))
                    break
                else:
                    prot.append(code[codon])
    return ORFs

def revc(s):
    s = s[::-1]
    return s.translate(str.maketrans('ACGT','TGCA'))

ORFs = find_ORFs(s)
cORFs = find_ORFs(revc(s))


with open('rosalind_orf_out.txt', 'w') as f:
    f.write('\n'.join(set(ORFs + cORFs)))