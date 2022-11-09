a = input('введите массив').split()
i = int(input('введите 1 шаг'))
j = int(input('введите 2 шаг'))
del a[i:j-1]
print(a)
for i in range(i,j-1):
    a.append(0)
print(a)