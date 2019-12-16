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

strings = FASTA_parse('rosalind_grph.txt')
with open('rosalind_grph_out.txt', 'w') as f:
    for i in strings.keys():
        for j in strings.keys():
            if strings[i] != strings[j]:
                if strings[i][-3:] == strings[j][:3]:
                    f.write(i+' '+j+'\n')