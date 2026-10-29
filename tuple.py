Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a=(3, 3.4, "python", 6+8j, True, False)
>>> a
(3, 3.4, 'python', (6+8j), True, False)
>>> a=(3, 3.4, "python", 6+8j, True, False, "python")
>>> a
(3, 3.4, 'python', (6+8j), True, False, 'python')
>>> a.index('python')
2
>>> a.count(3)
1
a
>>> a.count('python')
2
