import numpy as np
def main():
    # расстановка * по ходу ладьи на 2 клетки
    def set_s(matrix, x, y):
        # Устанавливаем символ влево
        if y-2 >= 0:
            matrix[x][y-1] = '*'
            matrix[x][y-2] = '*'

        # Устанавливаем символ вправо
        if y+2 < len(matrix):
            matrix[x][y+1] = '*'
            matrix[x][ y+2] = '*'

        # Устанавливаем символ вверх
        if x-2 >= 0:
            matrix[x-1][y] = '*'
            matrix[x-2][ y] = '*'

        # Устанавливаем символ вниз
        if x+2 < len(matrix):
            matrix[x+1][ y] = '*'
            matrix[x+2][ y] = '*'

        return matrix
    # расстановка * по ходу коня
    def set_n(matrix, x, y):
        # Устанавливаем символ влево
        
        if (y-1) >= 0 and (x-2) >=0:
            matrix[x-2][y-1] = '*'

        if (y-2) >= 0 and (x-1) >=0:
            matrix[x-1][y-2] = '*'

        if (y+2) <N-1 and (x-1) >=0:
            matrix[x-1][y+2] = '*'
        if (y-2) >= 0 and (x+1) <N-1:
            matrix[x+1][y-2] = '*'
        if (y-1) >= 0 and (x+2) <N-1:
            matrix[x+2][y-1] = '*'
        if (y+1) <N-1 and (x+2) <N-1:
            matrix[x+2][y+1] = '*'
        if (y+2) <N-1 and (x+1) <N-1:
            matrix[x+1][y+2] = '*'
        return matrix
    # создание матрицы с расствлеными * и #
    def replace_element(matrix, x, y,gp):
        for i,j in gp:
            matrix[i][j] = '#'
            matrix=set_s(matrix,i,j)
            matrix=set_n(matrix,i,j)
        matrix[x][y] = '#' 
        matrix= set_s(matrix,x,y)
        matrix= set_n(matrix,x,y)
        return matrix
    # проверка на бой фигур
    def check(x, y, mas, N):
        for y1 in range(0, N - y):
            if y1 < 3 and mas[x][y1 + y]:
                return False
        for x1 in range(0, N - x):
            if x1 < 3 and mas[x1 + x][y]:
                return False
        for x1 in range(0, x + 1):
            if x - x1 >= 0 and x1 < 3 and mas[x - x1][y]:
                return False
        for y1 in range(0, y + 1):
            if y - y1 >= 0 and y1 < 3 and mas[x][y - y1]:
                return False
        if x >= 2 and y >= 1 and mas[x - 2][y - 1]:
            return False
        if x >= 2 and y < N - 1 and mas[x - 2][y + 1]:
            return False
        if x >= 1 and y >= 2 and mas[x - 1][y - 2]:
            return False
        if x >= 1 and y < N - 2 and mas[x - 1][y + 2]:
            return False
        if x < N - 2 and y < N - 1 and mas[x + 2][y + 1]:
            return False
        if x < N - 1 and y >= 2 and mas[x + 1][y - 2]:
            return False
        if x < N - 1 and y < N - 2 and mas[x + 1][y + 2]:
            return False
        if x < N - 2 and y >= 1 and mas[x + 2][y - 1]:
            return False
        return True
    # перебор всех возможных последовательностей
    def rec(x, y, mas, N, cont, L, a, otv1):
        for p in range(x, N):
            for i in range(y, N):
                if cont >= L:
                    for j in range(L):
                        otv2.append(list(otv1[j].split(',')))
                    otv1[-1] = "h"
                    otv2.append("")
                    return 1
                if check(i, p, mas, N) == 1:
                    otv1[cont] = str(i) + "," + str(p)
                    cont += 1
                    mas[i][p] = 1
                    a += rec(i, p, mas, N, cont, L, a, otv1)
                    cont = 0
                    mas[i][p] = 0
        return a
    # считывание данных с файла
    fin = open("input.txt", "r")
    fout = open("output.txt", "w")
    N, L, K = map(int, fin.readline().split())
    mas = [[0] * N for _ in range(N)]
    otv1 = [0] * L
    gp=[]

    for _ in range(K):
        x, y = map(int, fin.readline().split())
        x+=1
        y+=1
        g1=[x-1,y-1]
        gp.append(g1)
        mas[x - 1][y - 1] = 1

    otv2 = []
    # вызов функции
    rec(0, 0, mas, N, 0, L, 0, otv1)
    arr=['0']*N
    for i in range (N):
        arr[i]=['0']*N
    # вывод результата в консоль и запись в файл
    for p in otv2:
        if p!='':
            x1=int(p[0])
            y1=int(p[1])
            arr=replace_element(arr, x1, y1,gp)
            for d in arr:
                print (d)
        else:
            print()
        for i in range (N):
            arr[i]=['0']*N
        fout.write(str(p) + "\n")

    fout.close()
if __name__=='__main__':
    main()