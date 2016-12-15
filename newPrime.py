# -*- coding:utf-8 -*-
__author__ = 'dlmyb'

from collections import deque
import time

primeList = deque([2,3])

def isPrime(num):
    for i in primeList:
        if i**2 > num:
            break
        if num % i == 0:
            return
    primeList.append(num)


def findPrime(maxNum):
    maxNum = (maxNum+1)/2*2-1
    # for i in range(primeList[-1],maxNum+1,2):
    #     isPrime(i)
    # range() 会占用大量空间,弃用
    i = primeList[-1]
    while i != maxNum:
        isPrime(i)
        i += 2
    return primeList

if __name__ == '__main__':
    num = [100,1000]
    for i in num:
        p = findPrime(i)
        print list(p)
    # t = time.time()
    # findPrime(10000000)
    # print time.time() - t






