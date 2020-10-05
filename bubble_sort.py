from array import *
a = array('i',[])
n = int(input("Enter the size of array: "))
for i in range(n):
    a.append(int(input("Enter the next value: ")))

for i in range(n-1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
