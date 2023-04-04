for x in range(0, 151):
    print (x)

for x in range(5, 1001,5):
    print(x)

for x in range(1,101):
    if x%10==0:
        print("Coding")
    elif x%5==0:
        print("CodingDojo")
    else:
        print(x)


sum = 0 
for x in range(500001):
    sum += x
print(sum)


num = 2018
while num > 0:
    print(num)
    num-=4


lowNum = 2
highNum = 9
mult = 3

for x in  range(lowNum,highNum+1):
    if x % mult ==0:
        print(x)