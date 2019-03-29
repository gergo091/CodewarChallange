def anagrams(word, words):
    strings = []
    res = ''.join(sorted(word))
    for s in words:
        rest = ''.join(sorted(s))
        if res == rest:
            strings.append(s)
    return strings


if __name__ == "__main__":
    print anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
    # Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
    # Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])