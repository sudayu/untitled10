
#!/usr/bin/env python
# filename: some.py
#-*- coding:utf-8 -*-
def process():
   for i in range(0, 100000):
        if i == 10000:
            f = open('state.txt', 'w')
            f.write(u"正在处理第%s条数据" % i)
            f.close()

