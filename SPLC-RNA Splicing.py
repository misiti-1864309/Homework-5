with open('RNA codon table.txt') as f:
    text = f.read().split()
code = {}
for i in range(0, len(text), 2):
    code[text[i]] = text[i+1]

introns = {}
with open('rosalind_splc.txt') as f:
    text = f.read()
    items = text.split('>')
    first = items[1].split('\n')
    s_id = first.pop(0)
    s = ''.join(first)
    for item in items[2:]:
        item = item.split('\n')
        string_id = item.pop(0)
        introns[string_id] = ''.join(item)

for intron in introns.values():
    s = s.replace(intron, '')
s = s.replace('T', 'U')    

prot = []
started = False
for i in range(0, len(s), 3):
    codon = s[i:i+3]
    if codon == 'AUG':
        started = True
    if started:
        if code[codon] == 'Stop':
            break
        else:
            prot.append(code[codon])
with open('rosalind_splc_out.txt', 'w') as f:
    f.write(''.join(prot))