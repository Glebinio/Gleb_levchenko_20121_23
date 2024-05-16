def main():
    import itertools
    def splt(l):
        # разбиение на списки
        l2=l.split()
        l1=[]
        # создание всех возможных перестановок
        p= itertools.permutations (l2)
        # перебор получившихся комбинаций
        for k in p:
            k=list (k)
            g=0
            # проверка на одинаковые комбинации
            for j in l1:
                if k==j:
                    g=1
            if g==0:
                l1.append(list(k))
        return (l1)
    assert splt('1 2 3')==[['1', '2', '3'], ['1', '3', '2'], ['2', '1', '3'], ['2', '3', '1'], ['3', '1', '2'], ['3', '2', '1']]
    assert splt('1 1 2')==[['1', '1', '2'], ['1', '2', '1'], ['2', '1', '1']]
    print (splt('0'))
    

if __name__=="__main__":
    main()