Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Indexing
a="vijayawada"
a[0]
'v'
a[4]
'y'
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'

a="I am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[6]
'n'
a[5]+a[6]
'in'
a[3]+a[4]
'm '
a[2]
'a'
a[2]+a[3]
'am'
a[0]
'I'
a[1]
' '
a[1]+a[4]+a[7]
'   '
a
'I am in class'

a="I am learning python full stack"
a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'ython '
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[6]+a[7]+a[8]+a[9]+a[10]
'earni'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
>>> a[21]+a[22]+a[23]+a[24]
'full'
>>> 
>>> b="Time is very precious"
>>> a[13]
' '
>>> a[14]
'p'
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]+a[21]
'python f'
>>> b[13]
'p'
>>> 

>>> b="Time is very precious"
>>> b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
>>> b[8]+b[9]+b[10]+b[11]
'very'
>>> b[0]+b[1]+b[2]+b[3]
'Time'
>>> b[5]+b[6]
'is'
>>> 
>>> #negative indexing
>>> a="Vijayawada is a royal city"
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'city'
>>> a[-15]+a[-14]
'is'
>>> 
>>> b="vizag is a city od destiny"
>>> b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
>>> b[-15]+b[-14]+b[-13]+b[-12]
'city'
>>> b[-26]
'v'
>>> b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'
