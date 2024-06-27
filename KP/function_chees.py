from numpy import array
date = []
vars: list
allVar: list
def rec(board, x, y, l, n, vars, allVar): #перебор вариантов по строкам и столбцам
    while True:#перебор всех ходов
        y += 1
        if y >= n: 
            y = 0
            x += 1
        if x >= n: 
            break
        if board[x][y] == 0:  #Если место доступно для хода, то ставим фигуры
            copy_board=array(board)
            copy_var = [i for i in vars]
            place_figure(copy_board, n, x, y, copy_var)#размещение фигуры
            if l - 1 == 0:#проверка на количество поставленных фигур
                allVar.append(copy_var)
                if len(allVar) == 1:
                    print_board_in_console(copy_board)
                continue
            # рекурсивный перебор
            rec(copy_board, x, y + 1, l - 1, n, copy_var, allVar)
def is_under_attack(board, x, y, n):#поиск возможных ходов
    #Ходы по ходу ладьи и коня
    
    get_attacked_cells(board, x + 2, y + 1,n)
    get_attacked_cells(board, x + 2, y - 1,n)
    get_attacked_cells(board, x - 2, y + 1,n)
    get_attacked_cells(board, x - 2, y - 1,n)
    get_attacked_cells(board, x + 1, y + 2,n)
    get_attacked_cells(board, x + 1, y - 2,n)
    get_attacked_cells(board, x - 1, y + 2,n)
    get_attacked_cells(board, x - 1, y - 2,n)
    get_attacked_cells(board, x - 1, y,n)
    get_attacked_cells(board, x - 2, y,n)
    get_attacked_cells(board, x + 2, y,n)
    get_attacked_cells(board, x + 1, y,n)
    get_attacked_cells(board, x, y - 1,n)
    get_attacked_cells(board, x, y - 2,n)
    get_attacked_cells(board, x, y + 1,n)
    get_attacked_cells(board, x, y + 2,n)



def get_attacked_cells(board, x, y, n):#записываем клетки с возможным ударом
    if not (0 <= x < n and 0 <= y < n):#проверка на выход за пределы поля
        return False
    if board[x][y] != 1:#проверка на поставленную фигуру
        board[x][y] = 2
        return True
    else:
        return True
def place_figure(board, n, x, y, vars):#размещение фигуры на доске
    board[x][y] = 1
    vars.append((x, y))
    is_under_attack(board, x, y, n)
def w_out(vars):#запись решений в файл
    with open("output.txt", "w") as f:
        if not len(vars):
            f.write("no solutions")
        else:
            for i_g in vars:
                f.writelines(f"{str(i)} " for i in i_g)
                f.writelines('\n')
    print("Количество решений:", len(vars))
    date.append(len(vars))
def print_board_in_console(board):#вывод доски
    list_board = []
    x = 0
    y = 0
    for s in board:
        y = 0
        for cell in s:
            if cell == 1:  # если стоит фигура, #
                list_board.append((x, y, 1))
            elif cell == 2:  # если клетка с возможным ходом *
                list_board.append((x, y, 2))
            else:  # если клетка пустая, 0
                list_board.append((x, y, 0))
            y += 1
        x += 1
    for m in board:
        s = ""
        for r in m:
            if r == 1:#если стоит фигура, #
                s += " " + '#'
            elif r == 2:#если клетка с возможным ходом, *
                s += " " + '*'
            else:#если клетка пустая, 0
                s += " " + '0'
        print(s)
    date.append(list_board)
def main():
    vars = []
    allVar = []
    with open("input.txt", "r") as f_f:
        n, l, k = map(int, f_f.readline().split())
        board = array([[0] * n for _ in range(n)])
        #Добавление расставленных фигур на доску
        for _ in range(k):
            x, y = map(int, f_f.readline().split())
            place_figure(board, n, x, y, vars)
    #Если нет фигур которые нужно поставить
    if l == 0:
        if not (len(vars) == 0):
            allVar.append(vars)
        print_board_in_console(board)
        return w_out(allVar)
    #подбираем расстановки
    rec(board, 0, -1, l, n, vars, allVar)
    w_out(allVar)
    return date
if __name__ == '__main__':
    main()
