def main():
    def sum_matrix (n,l,c):
        l1,m,l2=[],0,[]
        # поиск всех возможных сумм
        for i in range (len(l)):
            for j in range (i+1,len(l)):
                for k in range (j+1,len(l)):
                    for t in range (k+1,len(l)):
                        l1.append(l[i]+l[j]+l[k]+l[t])
                        m+=1
        # проверка на равенство или приближенность
        for d in l1:
            l2.append (abs(c-d))
            for i in range (len(l)):
                for j in range (i+1,len(l)):
                    for k in range (j+1,len(l)):
                        for t in range (k+1,len(l)):
                            if (l[i]+l[j]+l[k]+l[t])==l1[l2.index(min(l2))]:
                                g= (l[i],l[j],l[k],l[t])
                                break
        return (g,l1[l2.index(min(l2))])
    assert sum_matrix(5,[1, 2, 4, -5,-2],1) ==((1, 2, 4, -5), 2)
    assert sum_matrix(6,[4, -5, -7, 12,-2,5],-5) ==((4,-5,-7,5),-3)
    assert sum_matrix(7,[1,1,1,1,1,1,1],5) ==((1,1,1,1),4)

    print (sum_matrix (5,[1,3,0,-4,8],3))

    

if __name__=="__main__":
    main()