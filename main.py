#coding=utf-8

import os,re,time
import ast
import subprocess
import clear,initial

curpid =str(os.getpid())

respd=stin=['']*10
pos=[0]*10
stuans=[(['']*12)for i in range(12)]*150
kinds=['']*12

stuans,kinds=initial.init()
 

with open("T1.py","r") as f:
    cont =str(f.readlines())
    with open("resp.txt", "rt") as ff:
        respd = ff.readlines()
    with open('std1.txt', 'rt') as ff:
        stin =ff.readlines()

    num=1
    for match in re.finditer(re.compile(r'<.>'),cont):
        pos[num]=match.start();num=num+1

    num=num-1
    for i in range(1,num+1):
        compensate=0
        cnt =cont
        for j in range(1,num+1):
            if j!=i:

                add =str(stin[j-1].strip('\n'))
            else:
                add =str(respd[j-1].strip('\n'))
            with open('T1_'+str(i)+'.py','w') as f:
                cnt = cnt[:pos[j]+compensate] + add + cnt[pos[j]+compensate + 3:]
                writein=ast.literal_eval(cnt)
                f.writelines(writein)
                compensate=compensate+len(add)-3

ansprogrm={}
st=ed={}
flag =[0]*10
for i in range(1,num+1):
    st[i]=time.time()
    ansprogrm[i]=subprocess.Popen('py D:\\MINE\\code\\python\\judg\\T1_'+str(i)+'.py',shell=True,stdout=subprocess.PIPE)

ed =time.time()
ans=''
while ed-st[num]<0.5:
    mk =False
    for i in range(1,num+1):
        if flag[i] ==0:
            mk=True
            if ansprogrm[i].poll()==0:
                flag[i]=1
            elif ansprogrm[i].returncode==1:
                flag[i]=2
    if not mk:
        break
    ed = time.time()

for i in range (1,num+1):
    print(str(i))
    if flag[i]==0:
        print('RE')
        ansprogrm[i].kill()
    elif flag[i]==1:
        ans =''
        with open('std1out.txt','r') as f:
            ans=f.readline().strip('\n')
        if ans ==str(ansprogrm[i].stdout.read())[2:-5]:
            print('ACCEPTED!')
        else:
            print("WRONG ANSWER!")
    else:
        print('CE')

clear.clean(curpid,1,3)

# print(T1_1.pid)
# if flag==0:
#     T1_1.kill();print("RE")
# elif flag==2:
#     print("CE")
# else:
#     print(str(T1_1.stdout.read())[2:-5])
# clear.clean(curpid)

