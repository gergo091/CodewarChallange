import re

def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = re.split('[^a-zA-Z]', text.lower())
    joined_text = ''.join(s)
    result = []
    for i in range(0,len(joined_text),1):
        result.append(alphabet.index(joined_text[i])+1)

    return ' '.join(str(x) for x in result)

if __name__ == '__main__':
    print alphabet_position("The sunset sets at twelve o' clock.")
    # from random import randint
    # test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
    # test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

    # number_test = ""
    # for item in range(10):
    #     number_test += str(randint(1, 9))
    # test.assert_equals(alphabet_position(number_test), "")