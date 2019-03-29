NO_OF_CHARS = 256

def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+=1
    return count

def first_non_repeating_letter(string):
    count = getCharCountArray(string.lower())
    index = -1
    k = 0
 
    for i in string.lower():
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
    if index == -1:
        return ""
    else:
        return string[index]
    

if __name__ == "__main__":
    print first_non_repeating_letter('sTreSS')
    # Test.describe('Basic Tests')
    # Test.it('should handle simple tests')
    # Test.assert_equals(first_non_repeating_letter('a'), 'a')
    # Test.assert_equals(first_non_repeating_letter('stress'), 't')
    # Test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

    # Test.it('should handle empty strings')
    # Test.assert_equals(first_non_repeating_letter(''), '')

    # Test.it('should handle all repeating strings') 
    # Test.assert_equals(first_non_repeating_letter('abba'), '')
    # Test.assert_equals(first_non_repeating_letter('aa'), '')

    # Test.it('should handle odd characters')
    # Test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
    # Test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

    # Test.it('should handle letter cases')
    # Test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
    # Test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')