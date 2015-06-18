# -*- coding: utf-8 -*-
import pp
import time
job_server = pp.Server()
def N(a,b,c):
    import math
    def M(i):
        # 排除1、2、3、5基础数字干扰
        if i == 1:
            return False
        elif i == 2:
            return True
        elif i == 3:
            return True
        elif i == 5:
            return True
        # 使用末尾数来判断2和5的倍数
        if str(i)[-1] == '5' or str(i)[-1] == '0':
            return False
        elif int(str(i)[-1]) % 2 == 0:
            return False
        n = 3
        # 开始判断质数
        while n <= int(math.sqrt(i)):
            if i % n == 0:
                return False
            n = n+2
        return True
    L = []
    d = a
    # 采用埃氏筛法，找到一个质数写入L中，节省内存
    while a <= b:
        if M(a) == True:
            L.append(a)
        a = a+1
    c = str(c) + '.txt'
    fo = open(c,"w")
    fo.writelines(str(d)+'~'+str(b)+'\n')
    fo.writelines(str(L))
    fo.close()
minNum = input('Enter the min number:')
maxNum = input('Enter the max number:')
step = (maxNum-minNum)/8
print u'现在开始找出'+str(minNum)+u'~'+str(maxNum)+u'的质数'
time.clock()
# pp 模块的多线程写法
f1 = job_server.submit(N,(minNum,int(minNum+step),1))
f2 = job_server.submit(N,(int(minNum+step),int(minNum+step*2),2))
f3 = job_server.submit(N,(int(minNum+step*2),int(minNum+step*3),3))
f4 = job_server.submit(N,(int(minNum+step*3),int(minNum+step*4),4))
f5 = job_server.submit(N,(int(minNum+step*4),int(minNum+step*5),5))
f6 = job_server.submit(N,(int(minNum+step*5),int(minNum+step*6),6))
f7 = job_server.submit(N,(int(minNum+step*6),int(minNum+step*7),7))
f8 = job_server.submit(N,(int(minNum+step*7),maxNum,8))
r1 = f1()
r2 = f2()
r3 = f3()
r4 = f4()
r5 = f5()
r6 = f6()
r7 = f7()
r8 = f8()
print u'用时' + str(time.clock())
