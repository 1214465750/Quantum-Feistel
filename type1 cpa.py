import pandas as pd
import numpy as np
from itertools import *



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
    nst[-1]=state[0]
    nst[1:-1]=state[2:]

    nst[0]=rxor(state[0],state[1])
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


    for i in list_state:
       print(i)

    maxround = judge(list_state)
    print("maxround", maxround)

    return maxround


def judge(list):
    length=len(list)-1
    maxlength=-1
    list1=[[1,1,0],[1,1,1],[1,2,0],[1,2,1],]
    list2=[[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,1,1],[1,0,1],[2,1,0],[1,2,0],[2,2,0]]
    for i in range(length,0,-1):
        if list[i][0]==[3,3,0]:
            if list[i-1][0] in list1 and  list[i-1][1] in list2:
                maxlength=i
                break

    return maxlength

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
    for index_x,index_ab in pailie:
        print([index_x,index_ab])
        maxround=main(d, round, index_x, index_ab)
        if maxround>maxr:
            maxr=maxround
            list_max=[[index_x,index_ab]]
        elif maxround==maxr:
            list_max.append([index_x,index_ab])
    print('maxround',maxr+d-1)
    print('max_list',list_max)
    return None

if __name__ == '__main__':

    d=6
    round=10
    index_x=3
    index_ab=2
    tab=table()

    jiance(d,round)








