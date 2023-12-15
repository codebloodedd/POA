def twoscomplement(num):
    onescomplement = ""
    for i in num:
        if i == "0":
            onescomplement += "1"
        else:
            onescomplement += "0"

    return bin(int(onescomplement,2) + int("1",2)).replace("0b","")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

binn1 = bin(abs(num1)).replace("0b", "")
binn2 = bin(abs(num2)).replace("0b", "")

if len(binn1) < len(binn2):
    maxlen = len(binn2)
else:
    maxlen = len(binn1)

maxlen += 1

binn1 = binn1.zfill(maxlen)
binn2 = binn2.zfill(maxlen)

if num1 < 0:
    binn1 = twoscomplement(binn1)
if num2 < 0:
    binn2 = twoscomplement(binn2)

binn1twoscomp = twoscomplement(binn1)
binn1twoscomp = binn1twoscomp.zfill(maxlen)

print(binn1)
print(binn2)
print(binn1twoscomp)

print(binn1[0])

count = maxlen
m = binn1
mneg = binn1twoscomp
q = binn2
q1 = '0'
a = "0"
a = a.zfill(maxlen)

rightShift = ""

while count > 0:
    if q1 == "1" and q[maxlen -1] == "0":
        a = bin(int(a,2)+int(m,2)).replace("0b", "")
        if (len(a)>maxlen):
            a = a[1:]
        a = a.zfill(maxlen)
    elif q1 == "0"and q[maxlen -1] == "1":
        a = bin(int(a,2)+int(mneg,2)).replace("0b","")
        if (len(a)>maxlen):
            a = a[1:]
        a = a.zfill(maxlen)

    merged = a+q+q1
    rightShift = merged[0]
    for i in range(len(merged)-1):
        rightShift += merged[i]

    a = rightShift[:maxlen]
    q = rightShift[maxlen:maxlen*2]
    q1 = rightShift[-1]
    count -= 1

ans = a+q
minus = False
if ans[0] == '1':
    ans = twoscomplement(ans)
    minus = True

print(ans)

if minus:
    print(int(ans,2)*-1)
else:
    print(int(ans,2))    