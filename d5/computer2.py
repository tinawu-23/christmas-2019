with open('input.txt') as f:
    codes = [int(x) for x in f.readlines()[0].split(',')]

num = 5

i = 0
while i < len(codes):
    code = str(codes[i])
    if len(code) < 4:
        code = '0'*(4-len(code)) + code

    process1 = code[1]
    process2 = code[0]
    i += 1

    if code == '0099':
        exit()

    if code[-1] == '3':  # input
        codes[codes[i]] = num

    elif code[-1] == '4':  # output
        if len(code) > 1 and code[0] == '1':  # immediate
            print(codes[i])
        else:
            print(codes[codes[i]])
    
    elif code[-1] == '5':  # jump-if-true
        if process1 == '1':  # immediate
            num1 = codes[i]
        elif process1 == '0':  # position
            num1 = codes[codes[i]]
        i += 1
        if num1 != 0: 
            if process2 == '1':  # immediate
                i = codes[i]
            elif process2 == '0':  # position
                i = codes[codes[i]]
            continue


    elif code[-1] == '6':  # jump-if-false
        if process1 == '1':  # immediate
            num1 = codes[i]
        elif process1 == '0':  # position
            num1 = codes[codes[i]]
        i += 1
        if num1 == 0:
            if process2 == '1':  # immediate
                i = codes[i]
            elif process2 == '0':  # position
                i = codes[codes[i]]
            continue

    elif code[-1] == '7':  # less than
        if process1 == '1':  # immediate
            num1 = codes[i]
        elif process1 == '0':  # position
            num1 = codes[codes[i]]
        i += 1
        if process2 == '1':  # immediate
            num2 = codes[i]
        elif process2 == '0':  # position
            num2 = codes[codes[i]]
        i += 1
        if num1 < num2:
            codes[codes[i]] = 1
        else:
            codes[codes[i]] = 0

    elif code[-1] == '8':  # equals
        if process1 == '1':  # immediate
            num1 = codes[i]
        elif process1 == '0':  # position
            num1 = codes[codes[i]]
        i += 1
        if process2 == '1':  # immediate
            num2 = codes[i]
        elif process2 == '0':  # position
            num2 = codes[codes[i]]
        i += 1
        if num1 == num2:
            codes[codes[i]] = 1
        else:
            codes[codes[i]] = 0

    elif code[-1] == '2':  # multiply
        if process1 == '1':  # immediate
            num1 = codes[i]
        elif process1 == '0':  # position
            num1 = codes[codes[i]]
        i += 1
        if process2 == '1':  # immediate
            num2 = codes[i]
        elif process2 == '0':  # position
            num2 = codes[codes[i]]

        res = num1 * num2  # result

        i += 1
        codes[codes[i]] = res

    elif code[-1] == '1':  # addition
        if process1 == '1':  # immediate
            num1 = codes[i]
        elif process1 == '0':  # position
            num1 = codes[codes[i]]
        i += 1
        if process2 == '1':  # immediate
            num2 = codes[i]
        elif process2 == '0':  # position
            num2 = codes[codes[i]]

        res = num1 + num2  # result

        i += 1
        codes[codes[i]] = res
    i += 1