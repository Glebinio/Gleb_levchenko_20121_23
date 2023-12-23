from itertools import combinations
def main():
    def f(x):
        # создаем словарь с возможными значениями
        mb={'1' : '124', '2':'1235','3':'236',
        '4': '1457', '5':'24568','6':'3569',
        '7':'478', '8':'57890', '9':'689',
        '0':'08'}
        l1=[]
        l=[]
        l2=[]
        s=''
        # переводим все возможные значения в список
        for j in range (len(x)):
            for i in mb[x[j]]:
                l1.append (i)

# состовляем все возможные комбинации
        for i in combinations(l1, len(x)):
                 l2.append(i)
# проверяем комбинации на совпадение
        for i in l2:
            for j in range (len(i)):
                  s+=i[j]
            if s not in l:
                  l.append(s)
            s=''
        
        return (l)
        
    assert f('8')==['5', '7', '8', '9', '0']
    assert f('11')==['12', '14', '11', '24', '21', '22', '41', '42', '44']
    print (f('11'))
if __name__=="__main__":
    main()