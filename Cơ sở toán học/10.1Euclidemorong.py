a=int(input())
b=int(input())
a1=a
b1=b
q=0
r=0
x=0
y=0
x2=1
x1=0
y2=0
y1=1
print('|%-7s|%-7s|%-7s|%-7s|%-7s|%-7s|%-7s|%-7s|%-7s|%-7s|'%('   q   ','   r   ','   x   ','   y   ','   a   ','   b   ','  x2   ','  x1   ','  y2   ','  y1   '))
print('|%-7s|%-7s|%-7s|%-7s|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|'%('   -   ','   -   ','   -   ','   -   ',a,b,x2,x1,y2,y1))
while b>0:
  q=a//b
  r=a-q*b
  x=x2-q*x1
  y=y2-q*y1
  a=b
  b=r
  x2=x1
  x1=x
  y2=y1
  y1=y
  print('|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|'%(q,r,x,y,a,b,x2,x1,y2,y1))

d=a
x=x2
y=y2
print('d= {} , x <-- {} , y <-- {} '.format(d,a,b))
print('{}^-1 mod {} = {}'.format(a1,b1,x))
print('{}^-1 mod {} = {}'.format(b1,a1,y))