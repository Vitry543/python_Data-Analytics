Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
#dict{}
a={"name":"Mani", "year":2026, "month":10}
a
{'name': 'Mani', 'year': 2026, 'month': 10}
type(a)
<class 'dict'>
b={"name","Mani","year",2026}
b
{'year', 'name', 'Mani', 2026}
type(b)
<class 'set'>

#Methods
#keys()
a={"name":"Mani", "year":2026, "month":10}
a.keys()
dict_keys(['name', 'year', 'month'])
#value()
a.values()
dict_values(['Mani', 2026, 10])
#items()
a.items()
dict_items([('name', 'Mani'), ('year', 2026), ('month', 10)])
b={1:2, 3:4}
b.keys()
dict_keys([1, 3])
b.values()
dict_values([2, 4])
b.items()
dict_items([(1, 2), (3, 4)])

a={"course":"python", "code":"gnan","data":"coding"}
#accesing
a["course"]
'python'
a["python"]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a["python"]
KeyError: 'python'
a["code"]
'gnan'
#get()
a.get("code")
'gnan'
a.get("data")
'coding'
a
{'course': 'python', 'code': 'gnan', 'data': 'coding'}

#update
a={"yera":2026,"month":11}
a.update({"time":10})
a
{'yera': 2026, 'month': 11, 'time': 10}
a.update({"hour":10, "minute":5})
a
{'yera': 2026, 'month': 11, 'time': 10, 'hour': 10, 'minute': 5}
.update({"hour":10}, {"minute":5})
SyntaxError: invalid syntax
a.update({"hour":10}, {"minute":5})
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.update({"hour":10}, {"minute":5})
TypeError: update expected at most 1 argument, got 2
a
{'yera': 2026, 'month': 11, 'time': 10, 'hour': 10, 'minute': 5}


a={"colour":"Black","food":"Biryani","desert":"cake"}
a.setdefault("place","vja")
'vja'
a
{'colour': 'Black', 'food': 'Biryani', 'desert': 'cake', 'place': 'vja'}
a.setdefault("city")
a
{'colour': 'Black', 'food': 'Biryani', 'desert': 'cake', 'place': 'vja', 'city': None}

#pop()
a.pop()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("colour")
'Black'
a
{'food': 'Biryani', 'desert': 'cake', 'place': 'vja', 'city': None}
>>> #popitem()
>>> a.popitem()
('city', None)
>>> a
{'food': 'Biryani', 'desert': 'cake', 'place': 'vja'}
>>> 
>>> a={"hour":5, "min":23, "sec":5}
>>> a.copy()
{'hour': 5, 'min': 23, 'sec': 5}
>>> b=a.copy()
>>> b
{'hour': 5, 'min': 23, 'sec': 5}
>>> a.clear()
>>> a
{}
>>> 
>>> # do's and don't
>>> a={"name":"Mani","city":"vja", "name":"Mani"}
>>> a
{'name': 'Mani', 'city': 'vja'}
>>> a={"name":"Mani","city":"vja", "name":"sai"}
>>> a
{'name': 'sai', 'city': 'vja'}
>>> a={"name1":"Mani","city":"vja", "name2":"sai"}
>>> a
{'name1': 'Mani', 'city': 'vja', 'name2': 'sai'}
>>> 
>>> 
>>> #passing more tahn one value in a key
>>> a={"idnos":[10,20,30],"names":["Sai","Mani","B"],"marks":[23,43,34]}
>>> a
{'idnos': [10, 20, 30], 'names': ['Sai', 'Mani', 'B'], 'marks': [23, 43, 34]}
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['Sai', 'Mani', 'B'], [23, 43, 34]])
a
>>> .items()
SyntaxError: invalid syntax
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['Sai', 'Mani', 'B']), ('marks', [23, 43, 34])])
