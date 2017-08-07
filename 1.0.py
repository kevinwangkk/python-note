#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 由于Python源代码也是一个文本文件，
# 所以，当你的源代码中包含中文的时候，
# 在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，
# 加以上2行代码

print("hello world")

print(100+200)

print('100+200 =', 100+200)
#  逗号会输出成空格

# *******************************************************************************
# 输入/输出
# name = input()  # 和scanf类似
# print(name)

# name = input('please enter name:')
# print('hello',name)

# ********************************************************************************

# python对于大小写敏感

a = 100
if a > 100:         # 注意冒号 缩进
    print(a)
else:
    print(-a)

# ********************************************************************************

# 转义字符 \n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print("I'm OK")
print("I'm \"OK\"")     # 转义字符 \    \"  \'

print('\\\t\\')
print(r'\\\t\\')    # r'' 表示不转义

# ********************************************************************************

# 字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print(r'''line1    
line2
line3''')

# ********************************************************************************

# 布尔值 True False   and 与 or 或 not 非
# None 空值  并不能理解为0

# ********************************************************************************

# = 赋值符号
a = 100
print(a)
a = 'be'   # 这种变量本身类型不固定的语言称之为动态语言
print(a)

# 赋值符号先计算右侧的值
x = 10
x = x + 10
print(x)

# 用全部大写的变量名表示常量

# ********************************************************************************

# 除法
print(10/3)  # 3.3333333333333335
print(9/3)  # 3.0

print(10//3)  # 3   //地板除  只保留整数

print(10 % 3)  # 1   //取余

# ********************************************************************************

# 字符串 编码

# 如果统一成Unicode编码，乱码问题从此消失了。
# 但是，如果你写的文本基本上全部是英文的话，
# 用Unicode编码比ASCII编码需要多一倍的存储空间，
# 在存储和传输上就十分不划算。

# 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，
# 常用的英文字母被编码成1个字节，汉字通常是3个字节，
# 只有很生僻的字符才会被编码成4-6个字节。
# 如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间

print('编码')

print(ord('A'))   # 65 ord()函数获取字符的整数
print(ord('中'))  # 20013
print(chr(66))   # B  chr()函数把编码转换为对应的字符
print(chr(25991))  # 文

print('\u4e2d\u6587')  # 中文  20013 十进制 <-> 4e2d 十六进制

# encode() 可以编码为指定的bytes
print('AB'.encode('ascii'))     # b'AB'
print('中文'.encode('utf-8'))   # b'\xe4\xb8\xad\xe6\x96\x87'

# decode() 从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str
print(b'AB'.decode('ascii'))   # AB
print(b'AB'.decode('ASCII'))   # AB
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文

# ********************************************************************************

# len() 函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('ABC'))   # 3
print(len(b'ABC'))  # 3

print(len('中文'))    # 2
print(len('中文'.encode('utf-8')))    # 6

# ********************************************************************************
# 格式化字符串
print('hello,%s' % 'world')  # hello,world

print('Hi,%s,you have $%d.' % ('Kevin', 100))  # Hi,Kevin,you have $100.

# %d 整数  %f 浮点数  %s 字符串  %x 十六进制整数

print('\'%2d - %02d\'' % (3, 1))  # ' 3 - 01'
print('%.3f' % 3.1415926)  # 3.142

# 如果你不太确定应该用什么，%s永远起作用，
# 它会把任何数据类型转换为字符串

# ********************************************************************************

# list
classmates = ['michael', 'bob', 'tracy']
print(classmates)      # ['michael', 'bob', 'tracy']
print(len(classmates))  # 3

print(classmates[0])  # michael
print(classmates[1])  # bob
print(classmates[2])  # tracy

print(classmates[len(classmates)-1])  # 防止越界

print(classmates[-1])  # 直接获取最后一个元素
print(classmates[-2])  # 获取倒数第二个元素

classmates.append('adam')  # 在末尾追加元素 append
print(classmates)  # ['michael', 'bob', 'tracy', 'adam']

classmates.insert(1, 'jack')  # 在指定位置插入 insert
print(classmates)  # ['michael', 'jack', 'bob', 'tracy', 'adam']

print(classmates.pop())  # adam 删除末尾元素 pop
print(classmates)  # ['michael', 'jack', 'bob', 'tracy']

print(classmates.pop(1))  # jack 删除指定位置的元素
print(classmates)  # ['michael', 'bob', 'tracy']

classmates[1] = 'sarah'  # 可以直接赋值替换元素
print(classmates)  # ['michael', 'sarah', 'tracy']

# list里的元素类型可以不同
L = ['Apple', 123, True]

# list里包含list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))  # 4

print(s[2][0])  # asp  类似二维数组
print(s[2][1])  # php

P = []
print(len(P))  # 0m

# ********************************************************************************

# tuple 元组
# tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')

# “可变的”tuple   在tuple里定义一个list
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  # ('a', 'b', ['X', 'Y'])

# ********************************************************************************

# if
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# input() 返回的数据类型为str
# int() 将str转为整数

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# ********************************************************************************

# for
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:  # 注意冒号
    print(name)

# range()函数，可以生成一个整数序列  range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))  # [0, 1, 2, 3, 4]

Sum = 0
for x in range(101):
    Sum = Sum + x
print(Sum)

# while
Sum = 0
n = 99
while n > 0:
    Sum = Sum + n
    n = n - 2
print(Sum)

# break
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# ********************************************************************************

# dict 字典  使用键-值（key-value）存储 这个通过key计算位置的算法称为哈希算法（Hash）
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])  # 95

d['Adam'] = 67
print(d['Adam'])  # 67

# 'Thomas' in d  判断key是否存在dict中
print('Thomas' in d)  # False
print('Bob' in d)  # True

# 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
# 返回None的时候Python的交互式命令行不显示结果(交互式命令行)
print(d.get('Thomas'))  # None
print(d.get('Thomas', 3))  # 3

# 删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d.pop('Bob'))  # 75
print(d)  # {'Michael': 95, 'Tracy': 85, 'Adam': 67}  # Thomas 并不会加入进去

# ********************************************************************************

# set  set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1, 2, 3])
print(s)  # {1, 2, 3}

s = set([1, 1, 2, 2, 3, 3])
print(s)  # {1, 2, 3}

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)  # {1, 2, 3, 4}

# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)  # {1, 2, 3}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # {2, 3}
print(s1 | s2)  # {1, 2, 3, 4}

# ********************************************************************************

# str是不变对象，而list是可变对象

# ********************************************************************************

# 函数
# abs() 求绝对值函数
print(abs(100))
print(abs(-100))

# max()可以接收任意多个参数，并返回最大的那个
print(max(2, 3, 1, -5))  # 3

# ********************************************************************************

# 数据类型转换
# >>> int('123')
# 123
# >>> int(12.34)
# 12
# >>> float('12.34')
# 12.34
# >>> str(1.23)
# '1.23'
# >>> str(100)
# '100'
# >>> bool(1)
# True
# >>> bool('')
# False

# ********************************************************************************

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
# >>> a = abs # 变量a指向abs函数
# >>> a(-1) # 所以也可以通过a调用abs函数
# 1

# ********************************************************************************

# 定义函数
# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:


def my_abs(num):  # 定义一个函数上面需要两行空白 （PEP 8 编码规范）
    if num > 0:
        print(num)
    else:
        print(-num)

my_abs(-1)

# ********************************************************************************












