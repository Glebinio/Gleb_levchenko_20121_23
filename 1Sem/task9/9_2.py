def main():
    def func (s):
        # словарь с переводом римских в арабские
        num ={'I':'1',
            'V':'5',
            'X':'10',
            'L':'50',
            'C':'100',
            'D': '500',
            'M':'1000'}
        x=0
        # работа с исключениями
        if 'IV' in s:
            x+=4
            s=s.replace ('IV','',1)
        if 'IX' in s:
            x+=9
            s=s.replace ('IX','',1)
        if 'XL' in s:
            x+=40
            s=s.replace ('XL','',1)
        if 'XC' in s:
            x+=90
            s=s.replace ('XC','',1)
        if 'CD' in s:
            x+=400
            s=s.replace ('CD','',1)
        if 'CM' in s:
            x+=900
            s=s.replace ('CM','',1)
        # перевод из римских в арабские
        for k in s:
            x+=int(num[k])
        return (x)
    assert func('II')==2
    assert func('LVI')==56
    print (func("MCMXCIV"))
if __name__=="__main__":
    main()