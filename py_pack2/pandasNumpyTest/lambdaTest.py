import pandas as pd


cal  = lambda x,y: x+y
result = cal(1,2)
print(result)
##
a=[('b',3),('a',2),('d',4),('c',1)]
#a=sorted(a,key=lambda x:x[0])
##a=sorted(a,key=a[0]) 尝试用非lambda，不行
[('a',2),('b',3),('c',1),('d',4)]
print(a)
