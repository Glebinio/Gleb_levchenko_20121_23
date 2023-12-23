def main():
    def decode_morse (morse_text):
        MORSE_CODE = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
        '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
        '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
        '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS', ',':' '
        }

#работа с пробелами
        morse_text=morse_text.replace('   ',' , ')
        morse_symbols = morse_text.split()


        # Декодирование
        decoded_text = ''
        for symbol in morse_symbols:
            decoded_text += MORSE_CODE[symbol]

        return decoded_text
    assert decode_morse('.-') == 'A'
    assert decode_morse('--...') == '7'
    assert decode_morse('...-..-') == '$'
    assert decode_morse('.') == 'E'
    assert decode_morse('..') == 'I'
    assert decode_morse('. .') == 'EE'
    assert decode_morse('.   .') == 'E E'
    assert decode_morse('...-..- ...-..- ...-..-') == '$$$'
    assert decode_morse('----- .---- ..--- ---.. ----.') == '01289'
    assert decode_morse('.-... ---...   -..-. --...') == '&: /7'
    assert decode_morse('...---...') == 'SOS'
    assert decode_morse('... --- ...') == 'SOS'
    assert decode_morse('...   ---   ...') == 'S O S'
    print (decode_morse('...   ---   ...'))

if __name__=="__main__":
    main()