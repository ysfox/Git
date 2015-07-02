#!/usr/binenv python3
# -*- coding: utf-8 -*-
print('包含中文的Str');

print(ord('A'));
print(ord('中'));
print(chr(66));
print(chr(25991));
print('\u4e2d\u6587');

x = b'ABC'
print('ABC'.encode('ascii'));
print('中文'.encode('utf-8'));


print(b'ABC'.decode('ascii'));
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));

print(len('ABC'));
print(len('中文'));

print(len(b'ABC'));
print(len(b'\xe4\xb8\xad\xe6\x96\x87'));
print('中文'.encode('utf-8'));


print('Hello,%s' % 'world');
print('Hi,%s,you have $%d.' % ('Michael',10000000));

print('%2d-%02d' % (3,1));
print('%.2f' % 3.1415926);

print('Age:%s. Gender:%s' % (25,True));

print('grouth rage:%d%%' % 20);