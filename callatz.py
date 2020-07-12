#!/usr/bin/env python
# -*- coding:utf-8 -*-


def ergodic(ndict,nlist):
    """添加数据到字典"""
    for i in nlist:
        if i in ndict.keys():
            ndict[i] += 1
        else:
            ndict[i] = 1
    return ndict

def callatz(n,ndict = {},nlist = []):
    """
    卡拉兹猜想的实现
    """
    if n not in ndict.keys():
        """判断字典中是否存在 key == n,若存在,则说明n已经被覆盖,将其字典中对应的值+1即可返回"""
        if n != 1 :
            nlist.append(n)
            if n % 2 == 0:
                n //= 2
            else:
                n =(3 * n + 1)//2

            return(callatz(n,ndict,nlist))
        else:
            """递归出口"""
            nlist.append(n)
            ergodic(ndict,nlist)

            return(ndict)
    else:
        nlist.append(n)
        ergodic(ndict,nlist)

        return (ndict)
def judgeNum(numstr):

    numlist = [int(x) for x in list(numstr.split(' '))]

    ndict = {}
    """存储出现过的数字并存到字典ndict中"""
    for i in numlist:
        callatz(i,ndict,nlist = [])
    """字典里key对应的值等于1且存在于numlist的就是关键数。注意,遍历的是输入的字符串转化成的列表"""
    for i in numlist:
        if ndict[i] == 1:
            print(i,end=' ')
if __name__ == '__main__':

    judgeNum('3 5 6 7 8 11')




