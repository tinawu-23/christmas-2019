lowbound = 165432
highbound = 707912

cnt = 0

def valid(pw):
    i = 1
    doubleflag = False
    increaseflag = True
    while i < len(pw):
        if pw[i-1] > pw[i]:
            increaseflag = False
            break
        elif pw[i-1] == pw[i]:
            tmp = i
            while tmp < len(pw) and pw[tmp-1] == pw[tmp]:
                tmp += 1
            if tmp - i != 1:
                i = tmp
                continue
            else:
                doubleflag = True
        i += 1
    return doubleflag & increaseflag

for passcode in range(lowbound, highbound+1):
    if valid(str(passcode)):
        cnt += 1

print(cnt)