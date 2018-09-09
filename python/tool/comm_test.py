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
print("罗马数字转换int")
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanInt = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000};
        num = romanInt[s[0]];
        for i in range(1,len(s)):
            print(i)
            if romanInt[s[i]] > romanInt[s[i - 1]]:
                num += romanInt[s[i]] - 2 * romanInt[s[i - 1]];
            else:
                num += romanInt[s[i]];
        return num;
s = Solution()
print(s.romanToInt("MDCLXVI"))