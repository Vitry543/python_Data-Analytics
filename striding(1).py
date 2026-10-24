Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # striding
>>> a="cloud computing"
>>> a[::5]
'c u'
>>> a[3:11]
'ud compu'
>>> a[::8]
'cm'
>>> a[2::]
'oud computing'
>>> a[5:]
' computing'
>>> a[:12]
'cloud comput'
>>> 
>>> a="Machine learning"
>>> a[1:9:2]
'ahn '
>>> a[1:14:3]
'ai ai'
>>> a[2:13:4]
'cea'
>>> a[6:15:5]
'er'
>>> a[3:12:2]
'hn er'
>>> a[4:14:6]
'ia'
>>> 
>>> # Negative striding
>>> a="Python course"
>>> a[-1:-8:-2]
'ero '
>>> a[-2:-10:-3]
'son'
>>> a[-3:-13:-4]
'r t'
>>> a[-1:-12:-6]
'e '
>>> a[-4:-9:-2]
'ucn'

a[-9:-4:2]
'o o'
a[-13:-4:2]
'Pto o'

a[::-1]
'esruoc nohtyP'
a[0::]
'Python course'
a[0:]
'Python course'
a[-1::]
'e'
a[-1::-1]
'esruoc nohtyP'
