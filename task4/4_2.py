def main():
    def rotationx (x):
        # проверка - и 0
        s1,s2='',''
        if x[0]=='-':
            s1='-'
            x=x.replace('-','',1)
        if x[-1]=='0':
            x=x.replace ('0','',1)
        # переворот 
        for l in x:
            s2=l+s2
        s2=s1+s2
        # проверка 8 битности
        if int(s2)>128 or int(s2)<-128:
            return ('no solution')
        else:
            return (s2)
    assert rotationx('12')=='21'
    assert rotationx ('123')=='no solution'
    print (rotationx('-150'))
if __name__ == '__main__':
    main()