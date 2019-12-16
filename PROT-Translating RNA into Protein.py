with open('RNA codon table.txt') as f:
    text = f.read().split()
code = {}
for i in range(0, len(text), 2):
    code[text[i]] = text[i+1]

with open('rosalind_prot.txt') as f:
    s = f.readline().strip()

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
with open('rosalind_prot_out.txt', 'w') as f:
    f.write(''.join(prot))