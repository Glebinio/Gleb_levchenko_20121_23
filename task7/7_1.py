def main():
    def bank (n,a):
        sum1,sum2=0,0
        b1,b2,i=[],[],0

#сумма нечетных
        while i<n-1:
            if a[i][2]>a[i+1][2]:
                sum1+=a[i][2]
                b1.append(a[i][0])
                b1.append(a[i][1])
                i+=2
                
            else:
                sum1+=a[i+1][2]
                b1.append(a[i+1][0])
                b1.append(a[i+1][1])
                i+=3
                
#сумма четных
        for i in range (0,n,2):
            sum2+=a[i][2]
            b2.append(a[i][0])
            b2.append(a[i][1])

#сравнение
        if sum1>sum2:
            return (b1,sum1)
        else:
            return (b2,sum2)
    
    n=int(input('количество банков '))
    a1 = input("Banks ").split()
    a2 = input("sum ").split()

    a=[['',i,0] for i in range (n)]

    for i in range (n):
        a[i][0]=a1[i]
        a[i][2]=int(a2[i])
    for i in range (n):
        a[i]=tuple (a[i])
    print (a)

    l,k=bank(n,a)

    for i in range (0,len(l),2):
        print (l[i],' ',l[i+1])
    print ('сумма ', k)


if __name__=="__main__":
    main()