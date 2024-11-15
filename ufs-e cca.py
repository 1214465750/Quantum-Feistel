import pandas as pd
import numpy as np
from itertools import *
import os
import sys
import time
dict={0: 0, 1: 100, 2: 101, 3: 10, 4: 11, 5: 110, 6: 111, 7: 120, 8: 121, 9: 210, 10: 211, 11: 220, 12: 221, 13: 330}
redict={0: 0, 100: 1, 101: 2, 10: 3, 11: 4, 110: 5, 111: 6, 120: 7, 121: 8, 210: 9, 211: 10, 220: 11, 221: 12, 330: 13}
def xor1(a,b):
    c=tab[a][b]
    d=index_to_list(c)
    return d


def index_to_list(c):
    c = dict[c]
    d=[None] * 3
    d[0] = c // 100
    d[1] = (c % 100) // 10
    d[2] = c % 10
    return d
def list_to_index(a):
    b=100*a[0]+10*a[1]+a[2]
    c=redict[b]
    return c

def rxor(a,b):

    if a==[0,0,0] or a==[3,3,0]:
        c=a
    else:
        c=a.copy()
        c[2]=1



    c=list_to_index(c)

    b=list_to_index(b)
    d=xor1(c,b)


    return d

def rfc(state,d):
    nst=[None]*d
    for i in range(d):
        if i==0:
            nst[0]=state[d-1]
        else:
            nst[i]=rxor(nst[0], state[i -1])


    return nst
def main(d,round,index_x,index_ab):

    state=[[0,0,0]for i in range(d)]
    x=[1,0,0]
    ab=[0, 1, 0]
    state[index_x]=x
    state[index_ab] = ab
    list_state=[]
    list_state.append(state)

    for i in range(round):
        state=rfc(state,d)
        list_state.append(state)




    maxround,list_index = judge(list_state,d)

    return maxround,list_index,list_state


def judge(list,d):
    length=len(list)-1

    list1=[[1,1,0],[1,1,1],[1,2,0],[1,2,1],]
    list2=[[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,1,1],[1,0,1],[2,1,0],[1,2,0],[2,2,0]]

    list_index=[]
    maxlength=0
    for i in range(length,0,-1):
        if i < maxlength:
            break
        for j in range(d):
            if j==d-1:
                if  list[i][0] in list1 and  list[i-1][d-2] in list2 :
                    maxlength=i
                    list_index.append([i,j])

    return maxlength,list_index

def table():

    df = pd.read_excel('R-rule.xlsx', sheet_name='Sheet2')

    a = df.values


    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i, j] = redict[a[i][j]]




    return a

def jiance(d,round):
    l = [i for i in range(d)]
    pailie = list(permutations(l, 2))
    maxr=0
    list_max=[]
    for index_x,index_ab in pailie:
        maxround,list_index,list_state=main(d, round, index_x, index_ab)
        if maxround>maxr:

            os.system('cls')
            time.sleep(0.1)
            maxr=maxround
            list_max=[[[index_x,index_ab],list_index]]
            print([index_x, index_ab],maxround)
            for i in list_state:
                print(i)
        elif maxround==maxr:
            list_max.append([[index_x,index_ab],list_index])
            print([index_x, index_ab],maxround)
            for i in list_state:
                print(i)

    print('\nmaxround',maxr)
    print('max_list')
    for i in list_max:
        print(i)
    return None

if __name__ == '__main__':

    d=6
    round=7
    tab=table()
    jiance(d,round)







