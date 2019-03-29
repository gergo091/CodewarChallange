import re

def spin_words(sentence):
    list_string = re.split("\\s",sentence)
    result = []
    for s in list_string:
        if len(s) >= 5:
            result.append(s[::-1])
        else:
            result.append(s)
    return ' '.join(result)

if __name__ == "__main__":
    print spin_words("throw this in as an alternative just for the heck of it")
    #test.assert_equals(spin_words("Welcome"), "emocleW")