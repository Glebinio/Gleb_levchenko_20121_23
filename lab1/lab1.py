def main ():
# рекурсивный перебор всех возможных расстановок
    def operation (i,s,l,b,a,sum):
        nonlocal g
        nonlocal k
        if i==a:
            if sum==b:
                g=s
            else:
                k='no solution'
        else:
            s1=s+'+'+l[i+1]
            s2=s+'-'+l[i+1]
            sum1=sum+int(l[i+1])
            sum2=sum-int(l[i+1])
            operation (i+1,s1,l,b,a,sum1)
            operation (i+1,s2,l,b,a,sum2)

# чтение данных из файла
    with open('input.txt', 'r') as text:
        mylist = text.readline()
    text.close()
    g,k='',''
    l1=mylist.split()
    a=int(l1[0])-1
    b=int(l1[-1])
    l=l1[1:-1]
    m=''
    s=''
    for i in l:
        s+=i
    s1=l[0]
    # вызов функции
    operation (0,s1,s,b,a,int(l[0]))
# вывод данных на консоль и запись в файл
    if g!='':
        m=g+'='+str(b)
        print (g,'=',b)
    else:
        m=k
        print (k)
    with open('output.txt', 'w') as text:
        text.write(mylist+'\n'+m)

if __name__=='__main__':
    main()