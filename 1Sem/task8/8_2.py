from itertools import combinations
def main():
    def get_subsets(list):
        l=[]
        l1=[]
        # составление всех возможных комбинаций
        for j in range (len (list)):
            for i in combinations(list, j+1):
                l.append(i)
        # преобразование в множества
        for i in l:
            l1.append (set (i))
        return (len (l1),l1)
    assert (get_subsets([1,2,3,4]))==(15, [{1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}, {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}])
    assert (get_subsets(['a','b','c','d']))==(15, [{'a'}, {'b'}, {'c'}, {'d'}, {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'d', 'c'}, {'a', 'c', 'b'}, {'a', 'd', 'b'}, {'a', 'd', 'c'}, {'b', 'd', 'c'}, {'a', 'd', 'c', 'b'}])
    print (get_subsets(['a','b','c','d']))
if __name__=="__main__":
    main()