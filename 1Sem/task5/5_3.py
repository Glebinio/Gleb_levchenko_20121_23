def main():
    def check_brackets(string):
        brackets = {'(': ')', '{': '}', '[': ']'}
        open_brackets = []
        for symbol in string:
            if symbol in brackets:
                open_brackets.append(symbol)
            else:
                if not open_brackets or brackets[open_brackets.pop()] != symbol:
                    return False
        if open_brackets:
            return ''.join(open_brackets)
        else:
            return True

    assert (check_brackets('()[]{}'))==True
    # True
    assert (check_brackets('(]'))==False
    # False
    assert (check_brackets(')()())'))==False
    # '()()'
    print(check_brackets('{[()]{[()]}}'))
    # True
if __name__ == '__main__':
    main()
