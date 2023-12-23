def main():
    def reversed_strin(w):
        # Преобразуем входную строку в список слов
        words = w.split()

        # Инвертируем порядок слов в списке и преобразуем первую букву каждого слова
        # в заглавную, а остальные в строчные
        reversed_string = ' '.join(words[::-1]).capitalize()
        return (reversed_string)
    assert reversed_strin('пРивет мИР')=='Мир привет'
    assert reversed_strin(' it       was     cool    ')=='Cool was it'
    print(reversed_strin ('good'))
if __name__=="__main__":
    main()