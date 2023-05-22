#задача 2
# n=int(input('введите трехзначное число: '))
# a1 = int(n/100)
# a2 = int((n/10)%10)
# a3 = n%10
# sum = a1+a2+a3
# print(sum)


#задача4
# n = int(input("введите количество журавликов: "))
# if(n%6==0):
#     n1=int(n/6)
#     n2=int(n1*4)
#     print(f"{n1} {n2} {n1}")
# else:
#     print("невозможно посчитать сколько журавликов при таком условии сделают ребята")

#задача 6
# n =int(input("Введите шестизначное число: "))
# a1 =int(n/100000)
# a2 = int((n/10000)%10)
# a3 = int((n/1000)%10)
# a4 = int((n/100)%10)
# a5 = int((n/10)%10)
# a6 = int(n%10)
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# print(a6)
# sum1=a1+a2+a3
# sum2=a4+a5+a6
# print(sum1)
# print(sum2)
# if(sum1==sum2):
#     print('yes')
# else:
#     print('no')

# Задача 8
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')