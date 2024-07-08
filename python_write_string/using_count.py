variable = "GoodMorning"
s1 = ""
temp = variable[0]
count = 0
for i in variable:
    if i == temp:
        count += 1
    else:
        a = str(count) + temp
        s1 += a
        count = 1
        temp = i
a = str(count) + temp
s1 += a
print(s1)