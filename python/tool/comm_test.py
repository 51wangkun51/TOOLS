import os,sys
'''继承'''
class A(object):
    name="AA"
    def __init__(self):
        self.__private()
        self.public()
    def __private(self):
        print('A.__private()')
    def public(self):
        print('A.public()')
class B(A):
    def __private(self):
        print('B.__private()')
    def public(self):
        print('B.public()')
b = B()
print("--------------------------------------------------")
a = A()
print("--------------------------------------------------")
print("\n".join(dir(A)))
print("--------------------------------------------------")
print(b.name)