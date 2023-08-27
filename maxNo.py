n = int(input("Size of array: "))
arr = []

for i in range(n):
    arr.append(int(input()))
max=arr[0]
for i in arr:
    if max<i:
        max=i
print("Greatest number is: ",max)

