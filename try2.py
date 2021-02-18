#1
a = 28
b = 14
c = (input("выбери знак, '+, -, *, /:"))
print(c)
if c == "+":
    x = a + b
    print(x)
elif c == "-":
    x = a - b
    print(x)
elif c == "*":
    x = a * b
    print(x)
elif c == "/":
    x = a / b
    print(x)
else:
    print("выбран неверный знак!Попробуй выбрать приведенные знаки!")

#2
x = 10
y = 5
q = (x - y)/(1+(x*y))
print(q)


#3
l_rebra = 7
V_kube =l_rebra**3
S_kube_1_s = l_rebra**2
print(V_kube, S_kube_1_s)

#4
import math
a1 = 9
b1 = 6
mid_arif = (a1+b1)/2
mid_geom = math.sqrt(a1*b1)
print(mid_arif, mid_geom)

#5
import  math
a2 = 9
b2 = 11
gip = math.sqrt(a2+b2)
s = 0.5*(a*b)
print(gip, s)