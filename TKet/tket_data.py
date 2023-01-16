

data = []
with open('result.txt') as f:
    lines = f.readlines()


    current = ''
    for l in lines:
        if not l.startswith('-'):
            val = l.split(':')
            v = val[1][:-1]
            current = current + str(v + ' ')
        else:
            #print(current)
            current = current[:-1]
            current = current + '\n'
            data.append(current)
            current = ''
            continue
        continue
with open('tket_and.txt', 'w') as f:
    f.write("#qubits rx ry rz cx p\n")
    for d in data:
        f.write(d)