def main():
  
    def longest_substring(s):
        # Создаем словарь, в котором будем хранить индексы символов
        char_dict = {}
        # Инициализируем переменные для отслеживания самой длинной подстроки и ее начального и конечного индексов
        max_length = 0
        start = 0
        end = 0
        
        for i in range(len(s)):
            # Проверяем, есть ли текущий символ в словаре и его индекс больше, чем начальный индекс текущей подстроки
            if s[i] in char_dict and char_dict[s[i]] >= start:
                # Обновляем начальный индекс подстроки
                start = char_dict[s[i]] + 1
            # Обновляем индекс текущего символа в словаре
            char_dict[s[i]] = i
            # Обновляем конечный индекс текущей подстроки
            end = i
            # Обновляем длину текущей подстроки
            length = end - start + 1
            # Если длина текущей подстроки больше, чем самая длинная подстрока, обновляем значения
            if length > max_length:
                max_length = length
                longest_sub = s[start:end+1]
       
        return longest_sub
    # Пример использования функции
    assert longest_substring('qweasdfdqw')=='qweasdf'
    assert longest_substring('aaaaaaa')=='a'

    print(longest_substring('prrker'))
if __name__=="__main__":
    main()