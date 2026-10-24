Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'

a="work until you succeed"
a[15:22]
'succeed'
a[11:14]
'you'
a[5:10]
'until'
a[0:4]
'work'

b="simple is better than complex"
b[9:15]
' bette'
b[10:16]
'better'
b[0:6]
'simple'
>>> b22:29]
SyntaxError: unmatched ']'
>>> b[22:29]
'complex'
>>> b[6:8]
' i'
>>> b[7:9]
'is'
>>> 
>>> 
>>> #negative slicing
>>> a="python id easy to learn"
>>> a[-13:-8]
'easy '
>>> a[-13:-9]
'easy'
>>> a[-23:-17]
'python'
>>> [-5:0]
SyntaxError: invalid syntax
>>> a[-5:]
'learn'
>>> 
>>> b="God is great"
>>> b[-5:0]
''
>>> b[-5:]
'great'
>>> b[-12:-9]
'God'
>>> b[-8:-6]
'is'
>>> 
>>> c="Python is a easy language"
>>> c[-13:-9]
'easy'
>>> c[-25:-19]
'Python'
>>> c[-18:-16]
'is'
>>> c[-8:]
'language'
