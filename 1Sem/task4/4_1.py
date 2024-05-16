def main():
    def rotationx (x):
        s1=''
        # переворот числа
        for i in range (len(x)):
            s1=x[i]+s1
        # проверка
        if s1==x:
            return (True)
        else:
            return (False)
    assert rotationx('121')==True
    print (rotationx('123'))

if __name__ == '__main__':
    main()