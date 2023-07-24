from __future__ import annotations
def foo(a: "str"): pass

print(foo.__annotations__)

class Base:
    a: int = 3
    b: str = 'abc'

class Derived(Base):
    pass

print(Derived.__annotations__)

import datetime as dt

"""
A = CurPer - StartDate
A = 1/31 - 1/1

today=dt.datetime.today()
print("                          Date:", today,"\n")
startdate=dt.
A=today-startdate
print(A)
"""
o=""

if isinstance(o, type):
    ann = o.__dict__.get('__annotations__', None)
else:
    ann = getattr(o, '__annotations__', None)

print(ann)