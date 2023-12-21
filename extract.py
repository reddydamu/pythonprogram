a=input('enter any number')
i=0
count=0
while i<len(a):
    if a(i) in "1,@,2,5,pass,1,5":
        count+=1
    i+=1
print(count)