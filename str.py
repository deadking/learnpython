# -*- coding: utf-8 -*-
# 格式化字符串的方法
# 1、%d	整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('Hi, %s, you have $%d.' % ('Michael', 1000000));

#2、format,它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125));

s1 = 72;
s2 = 85;
r = (s2-s1)/s2;

print('小明成绩提升的百分点 %f.' % (r*100));