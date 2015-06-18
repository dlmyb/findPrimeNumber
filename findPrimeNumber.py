# -*- coding: utf-8 -*-
import pp
import time
job_server = pp.Server()
def N(a,b,c):
    import math
    def M(i):
        if i == 1:
            return False
        elif i == 2:
            return True
        elif i == 3:
            return True
        elif i == 5:
            return True
        if str(i)[-1] == '5' or str(i)[-1] == '0':
            return False
        elif int(str(i)[-1]) % 2 == 0:
            return False
        n = 3
        while n <= int(math.sqrt(i)):
            if i % n == 0:
                return False
            n = n+2
        return True
    L = []
    d = a
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
f1 = job_server.submit(N,(minNum,int(minNum+step),1))
f2 = job_server.submit(N,(int(minNum+step),int(minNum+step*2),2))
f3 = job_server.submit(N,(int(minNum+step*2),int(minNum+step*3),3))
f4 = job_server.submit(N,(int(minNum+step*3),int(minNum+step*4),4))
f5 = job_server.submit(N,(int(minNum+step*4),int(minNum+step*5),5))
f6 = job_server.submit(N,(int(minNum+step*5),int(minNum+step*6),6))
f7 = job_server.submit(N,(int(minNum+step*6),int(minNum+step*7),7))
f8 = job_server.submit(N,(int(minNum+step*7),maxNum,8))
# f9 = job_server.submit(N,(50000000,56250000,9))
# f10 = job_server.submit(N,(56250000,62500000,10))
# f11 = job_server.submit(N,(62500000,68750000,11))
# f12 = job_server.submit(N,(68500000,75000000,12))
# f13 = job_server.submit(N,(75000000,81250000,13))
# f14 = job_server.submit(N,(81250000,87500000,14))
# f15 = job_server.submit(N,(87500000,93750000,15))
# f16 = job_server.submit(N,(93750000,100000000,16))
r1 = f1()
r2 = f2()
r3 = f3()
r4 = f4()
r5 = f5()
r6 = f6()
r7 = f7()
r8 = f8()
# r9 = f9()
# r10 = f10()
# r11 = f11()
# r12 = f12()
# r13 = f13()
# r14 = f14()
# r15 = f15()
# r16 = f16()
print u'用时' + str(time.clock())