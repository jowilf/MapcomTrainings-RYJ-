filename = 'bug.in'
with open(filename, 'r') as f:
    t = int(f.readline())
    for i in range(t):
        n,x,y=map(int,f.readline().strip().split())
        num=1
        solu=[]
        if y==1:
            while(n!=0):
                if x==num:
                    num+=1
                solu.append(num)
                num+=1
                n-=1
        else:
            if( x<=n):
                for i in range(n):
                    solu.append(i+1)
            else:
                while(n>1):
                    solu.append(num)
                    num+=1
                    n-=1
                solu.append(x)
        print(' '.join(map(str,solu)))
"""
        else:
            if x<=n:
                for i in range(n):
                    solu.append(i+1)
            else:
                n-=1
                while(n>1):
                    solu.append(num+1)
                solu.append(x)
        print(solu)
"""