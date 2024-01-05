num = float(input("enter num: "))
_round_ = int(input("enter round: "))

obj = {
    "start":0,
    "unit":0.1
}

i = 0
while True:
    i+=1
    if i * i > num:
        i = i-1
        obj["start"] = i
        break

for i in range(1,_round_+1):
    myx = obj['start']
    unit = obj["unit"]
    while myx*myx < num:
        myx+=unit
    myx-=unit
    obj['unit'] = unit*10**-1
    obj["start"] = myx
    myx = round(myx,_round_)

print(myx)