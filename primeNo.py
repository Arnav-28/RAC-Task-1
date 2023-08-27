n = int(input("Size of array: "))
arr = []
primeArr=[]

for i in range(n):
    arr.append(int(input()))

for num in arr:
    if num>1:
        flag=True
        for i in range(2,int(num/2)+1):
            if (num%i==0):
                flag=False
                break
        if flag:
            primeArr.append(num)

print(primeArr)