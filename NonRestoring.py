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

maxlen = len(binn1)

binn1 = binn1.zfill(maxlen)
binn2 = binn2.zfill(maxlen+1)

binn2twoscomp = twoscomplement(binn2)
binn2twoscomp = binn2twoscomp.zfill(maxlen)

count = maxlen
m = binn2
mNeg = binn2twoscomp
q = binn1
a = "0"
a = a.zfill(maxlen+1)
leftShift = ""

while count>0:
    merged = a+q
    leftShift = merged[1:]
    a = leftShift[:maxlen+1]
    if a[0] == "0":
        a = bin(int(a,2)+int(mNeg,2)).replace("0b","")
        if len(a)>maxlen+1:
            a = a[1:]
        a = a.zfill(maxlen+1)
    else:
        a = bin(int(a,2)+int(m,2)).replace("0b","")
        if len(a)>maxlen+1:
            a = a[1:]
        a = a.zfill(maxlen+1)

    leftShift = a+q[1:]
    
    if a[0] == "1":
        leftShift += "0"
    else:
        leftShift += "1"

    a = leftShift[:maxlen+1]
    q = leftShift[maxlen+1:]
    count -= 1

if a[0] == "1":

    a = bin(int(a,2)+int(m,2)).replace("0b","")
    if len(a) > maxlen+1:
        a = a[1:]

print(int(q,2))
print(int(a,2))
