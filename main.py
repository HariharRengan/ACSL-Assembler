def assembler(arr):
    acc = 0
    d = {}
    i = 0
    while True:
        label, op, loc = arr[i]
        if op == 'LOAD':
            acc = int(d[loc])
        elif op == 'STORE':
            d[loc] = acc
        elif op in ['ADD', 'SUB', 'MULT', 'DIV']:
            if op == 'ADD':
                acc += int(loc[1:]) if loc[0] == '=' else int(d[loc])
            elif op == 'SUB':
                acc -= int(loc[1:]) if loc[0] == '=' else int(d[loc])
            elif op == 'MULT':
                acc *= int(loc[1:]) if loc[0] == '=' else int(d[loc])
            elif op == 'DIV':
                acc = acc // (int(loc[1:]) if loc[0] == '=' else int(d[loc]))
        elif op in ['BG', 'BE', 'BL', 'BU']:
            if op == 'BG' and acc > 0:
                i = [k for k, i in enumerate(arr) if i[0] == loc][0] - 1
            elif op == 'BE' and acc == 0:
                i = [k for k, i in enumerate(arr) if i[0] == loc][0] - 1
            elif op == 'BL' and acc < 0:
                i = [k for k, i in enumerate(arr) if i[0] == loc][0] - 1
            elif op == 'BU':
                i = [k for k, i in enumerate(arr) if i[0] == loc][0] - 1
        elif op == 'READ':
            d[loc] = input()
        elif op == 'PRINT':
            print(d[loc])
        elif op == 'DC':
            d[label] = loc
        elif op == 'END':
            break
        i += 1

arr = [
    ["", "READ", "X"],
    ["", "LOAD", "X"],
    ["TOP", "SUB", "=1"],
    ["", "BE", "DONE"],
    ["", "STORE", "A"],
    ["", "MULT", "X"],
    ["", "STORE", "X"],
    ["", "LOAD", "A"],
    ["", "BU", "TOP"],
    ["DONE", "PRINT", "X"],
    ["", "END", ""]
]

assembler(arr)
