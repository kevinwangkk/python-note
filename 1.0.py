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
print(10/3) # 3.3333333333333335
print(9/3)  # 3.0

print(10//3) # 3   //地板除  只保留整数

print(10%3)  # 1   //取余

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

L = []
print(len(L))  # 0m

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
# ********************************************************************************
# ********************************************************************************
# ********************************************************************************






