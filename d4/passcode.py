lowbound = 165432
highbound = 707912

cnt = 0

def valid(pw):
    doubleflag = False
    increaseflag = True
    i = 1
    while i < len(pw):
        if pw[i-1] > pw[i]:
            increaseflag = False
            break
        elif pw[i-1] == pw[i]:
            doubleflag = True
        i += 1
    return doubleflag & increaseflag

for passcode in range(lowbound, highbound+1):
    if valid(str(passcode)):
        cnt += 1

print(cnt)
