#Вводим сколько хотим конфет и пакетов

#Создаем функцию
def main():
    def c(candies, packages):
        if packages > candies:
            return "No solution"
        elif packages == candies:
            return 1
        else:
            chislitel = 1
            znamenatel = 1
            #вычисляем факториал числителя
            for i in range(candies, candies - packages, -1):
                chislitel *= i
            #вычисляем факториал знаменателя
            for i in range(1, packages + 1):
                znamenatel *= i
            #Возвращаем количество комбинаций
            return chislitel // znamenatel
    #Выводим результат того, что ввел пользователь

#Ввыводим результат

    assert c(5,3) == 10
    assert c(3,5) == 'No solution'
    assert c(4,4) == 1
    print(c(4,4))
if __name__=="__main__":
    main()