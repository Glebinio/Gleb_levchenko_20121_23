def main():
    def srt(w):
        l=[]
        o=[]
        p=[]
        k=0
        y=[]
        # перебор всех слов
        for i in range (len(w)-1):
            for j in range (i+1,len(w)):
                # если длина слов одинаковая
                if len(w[i])==len (w[j]):
                    # сортируем слова
                    s1=sorted(w[i])
                    s2=sorted(w[j])
                    # если отсортированные слова одинаковые
                    if s1==s2:
                        # записываем
                        o.append (w[i])
                        o.append (w[j])
                        l.append(list(o))
                        o=[]
                        p.append (w[i])
                        p.append (w[j])
            # если у слова не нашлось совпадений, тоже записываем
            if w[i] not in p:
                y.append (w[i])
                l.append (y)
                y=[]
            # проверка последнего слова в исходном списке
            if i==(len(w)-2):
                if w[j] not in p:
                    y.append (w[i+1])
                    l.append (y)
                    y=[]
        return (l)

    assert srt(["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"])==[['qwe', 'ewq'], ['asd', 'dsa'], ['dsas'], ['qwee'], ['zxc', 'cxz'], ['xxz'], ['z'], ['s'], ['qweasdzxc'], ['zzxc']]
    print (srt(["a","a",""]))

if __name__=="__main__":
    main()