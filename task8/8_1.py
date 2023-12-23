def main():
    
    def ls (s1,s2):

    
        s1=set(tuple(list1))
        s2=set(tuple(list2))
# Количество элементов, присутствующих в обоих списках
        k1=(len(s1.intersection(s2)))
# Количество элементов, присутствующих только в одном списке
        k2=(len(s1.symmetric_difference(s2)))
# Количество оставшихся элементов в list1 после извлечения элементов из list2
        k3=(len(s1.difference(s2)))
# Количество оставшихся элементов в list2 после извлечения элементов из list1
        k4=(len(s2.difference(s1)))
        return (k1,k2,k3,k4)
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    assert (ls(list1,list2))==(3, 19, 9, 10)
    print (ls(list1,list2))
if __name__=="__main__":
    main()