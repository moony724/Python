import numpy as np

### 중복 삭제
a = [1,2,3]
b = [4,5,6]
c = [1,2,3,1,2,]
d = [3,3,4,5,6,6,6,7,8,8,9,]
print(a)
print(b)
print(c)
print(d)
print()

new_c = []
for i in c:
    if i not in new_c:
        new_c.append(i)
print(new_c)

new_d = []
for i in d:
    if i not in new_d:
        new_d.append(i)
print(new_d)



### 합집합 구하기
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

e = [1,2,3]
f = [2,3,4,5,6]
k = []
for i in e:
    if i not in f:
        k.append(i)
print(k)
k = k+f
print(k)





### 교집합 구하기
a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)





### 차집합 구하기
a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c)

d = [1,2,3]
e = [2,3,4,5,6]
f = a+[]
for i in e:
    if i in d:
        f.remove(i)
print(f)




### 여집합 구하기
u = [1,2,3,4,5]
a = [1,2,3]
a_com = []
for i in u:
    if i not in a:
        a_com.append(i)
print(a_com)


g = [1,2,3,4,5]
b = [1,2,3]
rest = g+[]
for i in g:
    if i in b:
        rest.remove(i)
print(rest)




### 소수 알아보기
a = 17
a_prime = True
for i in range(2,a):
    if a % i == 0:
        a_prime = False
if a_prime == True:
    print("%d is prime" %a)
else:
    print("%d is not prime" %a)




### 약수
a = 24
b = range(1,a)
factors = []
for i in b:
    if a % i == 0:
        factors.append(i)
factors.append(a)
print(factors)




### 최대공약수
a = 24
aa = range(1,a)
a_factors = []
for i in aa:
    if a % i == 0:
        a_factors.append(i)
a_factors.append(a)
print(a_factors)

b = 36
bb = range(1,b)
b_factors = []
for i in bb:
    if b % i == 0:
        b_factors.append(i)
b_factors.append(b)
print(b_factors)

common = []
for i in a_factors:
    if i in b_factors:
        common.append(i)
common.sort()
print(common[-1])



### 최소공배수
a = 24
b = 36
M = a+b
GCD = common[-1]
LCN = M / GCD
print("%d and %d `s LCN is %d" %(a, b, LCN))