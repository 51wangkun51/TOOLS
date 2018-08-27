import django
class A():
    name = "aaa"
    def __str__(self):
        return self.name

a = A()
print(a)