def main():

    def print_zigzag_string(string, rows):
        # анализ строки
        if rows == 1 or len(string) <= rows:
            return string
        zigzag = [''] * rows
        index = 0
        step = 1
        #формирование строки
        for char in string:
            zigzag[index] += char
            if index == 0:
                step = 1
            elif index == rows - 1:
                step = -1
            index += step
        return ''.join(zigzag)
    assert print_zigzag_string('перфекционист', 3)=='пеотефкинсрци'
    assert print_zigzag_string('перфекционист', 4)=='пцтекисреоифн'
    print (print_zigzag_string('перфекционист', 3))


if __name__=="__main__":
    main()