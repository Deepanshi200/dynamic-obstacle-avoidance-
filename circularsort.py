
def circularsort(listt):
    import matplotlib.pyplot as plt


    t = int(input("Enter the number of points"))
    rr=[]
    l=[]
    e=[]
    d=[]
    a=[]
    for i in range(t):
        print("Enter x co-ordinate of "+str(i)+" point")
        tx = float(input())
        print("Enter y co-ordinate of "+str(i)+ " point")
        ty= float(input())
        rr.append(tx)
        rr.append(ty)
        l.append(rr)
        rr=[]
    for rr in l:
        if(rr[1]>0):
            d.append(rr)
        else:
            a.append(rr)
    #print(a[0])
    #print(d)

    for i in range(len(a)):
        for j in range(0,len(a)-1):


            if((a[j][1])<(a[j+1][1])):


                t = a[j]
                a[j]=a[j+1]
                a[j+1]=t
    for i in range(len(d)):
        for j in range(0,len(d)-1):
            if((d[j][1])<(d[j+1][1])):
                t = d[j]
                d[j]=d[j+1]
                d[j+1]=t
    print(a)
    print(d)
    a=a+d[::-1]
    print(a)
    tt=[0,0]
    for k in a:

        
        plt.scatter(k[0],k[1],500,marker='*')
        plt.plot([tt[0],k[0],],[tt[1],k[1]])
        tt=k

    plt.show()
circularsort([10])
